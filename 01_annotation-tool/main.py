import os
import re
import json
import asyncio
import aiohttp
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# System prompts
system_prompt_1 = """
You are an information-retrieval expert fluent in Korean. You will receive five items; each item has (1) an unspaced Korean search query and (2) an array of five title+snippet strings returned by Google.
For each item, follow these steps exactly, then return one JSON object:
1. For each snippet, think step by step in 1-2 sentences whether it semantically contains the query. Allow for minor typos and close paraphrases, but be cautious--only consider it a match if the snippet directly and clearly relates to the core meaning of the query.
2. After your rationale, output one array "matches" of five Boolean values (true / false), one for snippet.

Respond strictly in the following JSON array format (no extra text):
[
  {
    "query": "<original query>",
    "matches": "[true, false, false, true, false]"
  },
  ...
]
"""

system_prompt_2 = """
You will be given a list of search queries submitted to a search engine. For each query, please classify the user's primary intent into one of the following three categories, choosing the most dominant intent if multiple apply:

1. Navigational: The user wants to visit a specific website, brand page, or official service page.
   (Example: "Naver," "Coupang customer service")

2. Transactional: The user intends to perform a specific action such as purchasing, downloading, booking, or watching something.
   (Example: "Buy used AirPods," "Netflix subscription," "vacuum cleaner head")

3. Informational: The user is looking for information or answers and the query does not fit into the above two categories.
   (Example: "Symptoms of depression," "Weather in Paris," "Supplements good for thyroid")

Additional instructions:
- If the query contains typos or abbreviations, infer the user's intent based on the most common or likely interpretation in context.
- Respond strictly in the following JSON array format (no extra text):

[
  {
    "query": "<original query>",
    "reasoning": "<clear explanation of why this query falls into the chosen category, based on words, phrases, or user intent>",
    "category": "Navigational / Transactional / Informational"
  },
  ...
]
"""

system_prompt_3 = """
You will be given a list of search queries entered into a search engine. For each query, extract **specific brand or product names** and **general product category names**.

Instructions:

1. Specific Brand or Product Name:
- Extract brand names, product names, or model numbers if present.
- Examples: 'Dior Lip Glow' → 'Dior', 'Apple Watch' → 'Apple Watch', 'Emtek GeForce GTX750' → 'Emtek GeForce GTX750'

2. General Product Category Name:
- Extract general product categories (only physical products; exclude services or software).
- Examples: 'meat', 'sneakers', 'Bluetooth earphones'

3. Compound Queries:
- For brand + product name, extract as one combined name.
- For brand + general product category, extract separately by type.
- Examples: 'Dior Lip Glow' → 'Dior', 'Lip Glow'; 'Musinsa Sneakers' → 'Musinsa', 'Sneakers'

4. Do not extract descriptions of product features or functions.
- Examples: 'laptop for design' → 'laptop', 'hypoallergenic dog chew' → 'dog chew', 'bidet bolt tightening' → 'bidet', 'kettlebell 16kg' → 'kettlebell'

5. N/A case:
- If neither a specific brand/product name nor a general product category applies, return 'N/A'.
- Example: 'pirate' → 'N/A'

Respond strictly in the following JSON array format (no extra text):
[
  {
    "query": "<original query>",
    "brand_or_product": "<extracted brand or product name or 'N/A'>",
    "general_product_category": "<extracted general product category name or 'N/A'>"
  },
  ...
]
"""
# ---------------------- GPT Call ----------------------
async def gpt_call(session, batch, system_prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    user_prompt = f"Query list = {batch}"
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    payload = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 1,
        "max_tokens": 1000
    }

    async with session.post(url, headers=headers, json=payload) as response:
        res = await response.json()
        try:
            return res["choices"][0]["message"]["content"]
        except Exception as e:
            print("Error:", e, "\nFull response:", res)
            return None

# ---------------------- Parse GPT Response ----------------------
# Parse response for system prompt 1
def parse_response_1(response: str) -> list:
    try:
        results = json.loads(response)
        return [item for item in results if 'query' in item and 'matches' in item]
    except json.JSONDecodeError:
        blocks = re.findall(r'\{[^{}]+\}', response)
        parsed = []
        for blk in blocks:
            try:
                obj = json.loads(blk)
                if {'query','matches'} <= obj.keys():
                    parsed.append(obj)
            except json.JSONDecodeError:
                continue
        return parsed

# Parse response for system prompt 2
def parse_response_2(response: str) -> list:
    try:
        results = json.loads(response)
        return [item for item in results if 'query' in item and 'reasoning' in item and 'category' in item]
    except json.JSONDecodeError:
        blocks = re.findall(r'\{[^{}]+\}', response)
        parsed = []
        for blk in blocks:
            try:
                obj = json.loads(blk)
                if {'query','reasoning','category'} <= obj.keys():
                    parsed.append(obj)
            except json.JSONDecodeError:
                continue
        return parsed

# Parse response for system prompt 3
def parse_response_3(response: str) -> list:
    required_keys = {'query', 'brand_or_product', 'general_product_category'}
    try:
        results = json.loads(response)
        # Return only items that contain all required keys
        return [item for item in results if required_keys <= item.keys()]
    except json.JSONDecodeError:
        # If full JSON parse fails, try to extract JSON objects via regex and parse individually
        blocks = re.findall(r'\{[^{}]+\}', response)
        parsed = []
        for blk in blocks:
            try:
                obj = json.loads(blk)
                if required_keys <= obj.keys():
                    parsed.append(obj)
            except json.JSONDecodeError:
                continue
        return parsed

# ---------------------- Main Workflow ----------------------
async def main(system_prompt, parse_response_func, input_csv, output_csv):
    # Load dataset from CSV into a list of dictionaries (rows)
    df = pd.read_csv(input_csv)
    rows = df.to_dict('records')

    batch_size = 5 # number of queries per GPT call 
    semaphore = asyncio.Semaphore(10) # limit of concurrent GPT calls
    tasks = []
    all_results = []

    async def sem_task(batch): # wrapper is used to limit the number of concurrent GPT calls
        async with semaphore:
            return await gpt_call(session, batch, system_prompt)
    # chunk dataset into batches of 5 rows, then adds an async task for each.
    async with aiohttp.ClientSession() as session:
        for idx in range(0, len(rows), batch_size):
            batch = rows[idx:idx + batch_size]
            tasks.append(asyncio.create_task(sem_task(batch)))

            if len(tasks) >= 20: # number of concurrent GPT calls
                for t in asyncio.as_completed(tasks):
                    try:
                        content = await t
                        if content:
                            parsed = parse_response_func(content)
                            all_results.extend(parsed)
                    except Exception as e:
                        print(f"[Error during GPT call or parsing]: {e}")
                tasks.clear()
        # Process any remaining tasks
        for t in asyncio.as_completed(tasks):
            try:
                content = await t
                if content:
                    parsed = parse_response_func(content)
                    all_results.extend(parsed)
            except Exception as e:
                print(f"[Error during GPT call or parsing]: {e}")

    pd.DataFrame(all_results).to_csv(output_csv, index=False)
    print(f"Finished writing to {output_csv}")

if __name__ == '__main__':
    # Example usage for prompt 1:
    # asyncio.run(main(system_prompt_1, parse_response_1, "input_data_1.csv", "results_1.csv"))

    # Example usage for prompt 2:
    # asyncio.run(main(system_prompt_2, parse_response_2, "input_data_2.csv", "results_2.csv"))

    # Example usage for prompt 3:
    # asyncio.run(main(system_prompt_3, parse_response_3, "input_data_3.csv", "results_3.csv"))
    pass
