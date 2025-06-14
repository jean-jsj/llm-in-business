# Case Study 1: Classify Search Queries

In this project, we used LLMs to categorize search queries as 'specific' or 'not specific' based on their level of detail and intent clarity
<br>

![table1](./table_1.png)
<br>

# Case Study 2: Evaluating LLM-User Conversations at Scale
Imagine you had thousands of **chat logs between end users and AI assistants**—how could you turn those free-form conversations into data you can actually analyze? By annotating LLM–user interaction data, we can ask deeper questions about how people and models communicate.

## LLM-User Interaction Can Be Unsafe

AI safety is trending everywhere—from news coverage to policy debates.In this project, we had an LLM review each user–model exchange and label it “safe” or “unsafe” in ten different risk categories:

- misinformation
- cyber attack
- criminal planning
- fraud and scams
- privacy breach
- copyright infringement
- violence or harassment
- self-harm
- sexual content
- inciting or abetting discrimination
<br><br>

![example1](./example_1.png)

![example2](./example_2.png)
<br>

## Why LLM Safety Evaluation Is Challenging
* Safety is **Subjective**: Perceptions of "safe" vary by person and culture, leading to conflicting views. Many outputs fall into a gray zone, neither clearly safe nor harmful.

* **No Ground Truth**: Unlike simple tasks (e.g., identifying a dog in a photo, detecting spam emails), safety has no fixed answer, with even experts disagreeing.
<br>

## Can LLMs Be Reliable Safety Judges?

The trending concept of **LLM-as-a-Judge**—using LLMs to evaluate outputs like safety or quality—is gaining traction in industry and academia. To ensure reliability, researchers focus on these key metrics:

* Human Alignment: LLMs must mirror human safety judgments, measured by agreement rates.
* Consistency: LLMs should deliver the same judgment for identical inputs every time.
* Calibration: LLM confidence (e.g., “90% sure this is safe”) must align with actual accuracy.

Note: LLM-as-a-Judge is a rapidly evolving field--for more on this research: (link)