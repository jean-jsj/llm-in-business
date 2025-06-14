# 📌 LLMs are Overtaking Traditional NLP Methods

Unstructured text—such as search queries, social media posts, and free-form responses—poses significant challenges for traditional analytical methods:

* Dictionary-Based Approaches often fail to capture the full spectrum of linguistic variation, as users express the same concept in multiple ways.
* Supervised Machine Learning requires extensive labeled data and contextual metadata, which are typically unavailable for ad-hoc text streams and infrequent query types.
 
Large language models (LLMs) are rapidly emerging as a compelling alternative!

* They understand subtle nuances in text so can classify on a more granular level
* they can classify based on criteria subjective in nature where no ground truth exists

### ✅ Text Classification Feasible with Traditional Tools
* **Sentiment Analysis**
"Label customer reviews as positive or negative"

* **Spam Detection**
"Flag incoming emails containing blacklisted URLs"

### ✅ Text Classification Only Practical with LLMs
* **Churn-Risk Signal**
"Classify customer message into risk types (e.g., switching for cost reasons, hate UI)"

* **Granular Intent Classification**
"Determine whether a customer is asking for a **refund**, **technical help**, etc"

* **Review Helpfulness**
"Read this customer review and tag it as **helpful**, **neutral**, or **unhelpful**"

* **Hallucination Detection**
"Does this response assert any facts not in the source doc?"
<br><br>

# 📌 Research Applications of LLMs

Empirical studies demonstrate that LLM outputs align closely with human raters across a range of tasks [(Bail, 2024)](https://www.pnas.org/doi/10.1073/pnas.2314021121)
* **Brand Similarity & Attribute Ratings**<br>
[Li et al. (2024)](https://pubsonline.informs.org/doi/abs/10.1287/mksc.2023.0454) uses LLMs to label brand similarity measures (e.g., clustering automotive brands by perceived closeness) and to assign product attribute ratings (such as luxury, reliability, and affordability)

* **Social Media Annotation**<br>
[Gilardi et al. (2023)](https://www.pnas.org/doi/10.1073/pnas.2305016120) uses LLMs to label tweets and news articles for relevance (to content moderation or politics), stance (e.g., support or opposition to Section 230), topic, and frame detection

* **Multilingual Psychological Constructs**<br>
[Rathje et al. (2024)](https://www.pnas.org/doi/10.1073/pnas.2308950121) uses LLMs to identify psychological constructs such as sentiment polarity, discrete emotions, offensiveness, and moral foundations in tweets spanning 12 languages

* **Social Science Constructs**<br>
[Ziems et al. (2024)](https://aclanthology.org/2024.cl-1.8/) uses LLMs to label text for persuasiveness (how convincingly a text argues), political ideology (e.g., left vs. right), populism, extremism, polarization, and other nuanced constructs drawn from political science and communication studies

* **Sentiment Detection**<br>
[Zhang et al., (2023)](https://arxiv.org/abs/2305.15005) go beyond simple positive/negative/neutral tags to label discrete emotions (anger, joy, sadness), aspect-based sentiment (e.g., service vs. quality in reviews), and subjectivity/intensity scores
<br><br>

# 📌 Best Practices & Tips

- **Use Fully-Specified Checklists**
  - Underspecified rubrics lead to lower inter-annotator agreement and higher subjective variance
  - Define every criterion in precise, unambiguous terms
  - Present the LLM with a literal "check the boxes" rubric

- **Favor Binary Judgments Over Likert Scales**
  - Defining distinct, objective criteria for each point on a 1-5 scale can be surprisingly difficult
  - Forcing binary decisions produces more reproducible annotations

- **Break Complex Tasks into Small, Binary Tasks ("Divide and Conquer" Approach)**
  - Example for tone evaluation: (1) Does the text use any profanity? (2) Is the greeting present ("Hello", "Hi")? (3) Are please and thank you included?

- **Prefer Pairwise or Ranking Prompts**
  - Ask the LLM "Which of the two responses is more accurate" instead of "Rate this response 1-5"

- **Guard Against LLM Biases**
  - Position Bias
  - Verbosity Bias
  - Self-enhancement Bias

- **Match Tasks to the Model's Strengths**
  - Leverage LLMs for judgments they have seen during pre-training
  - For highly specificalized domains, provide extrac context or domain examples
<br><br>

# 📌 Ensuring Validity of Your LLM tool

To ensure reliability, researchers focus on these key metrics:

- Human Alignment: LLMs must mirror human safety judgments, measured by agreement rates.
- Consistency: LLMs should deliver the same judgment for identical inputs every time.
- Calibration: LLM confidence (e.g., “90% sure this is safe”) must align with actual accuracy.
<br><br>

# 📌 Case Study 1: Classify Search Queries
[👉 Click to open a step-by-step demo](./search_query_specificity.ipynb)
<br>

In this project, we used LLMs to categorize search queries as 'specific' or 'not specific' based on their level of detail and intent clarity
<br>

# 📌 Case Study 2: Evaluating LLM-User Conversations at Scale
[👉 Click to open a step-by-step demo](./safety_evaluation.ipynb)
<br>

Imagine you had thousands of **chat logs between end users and AI assistants**—how could you turn those free-form conversations into data you can actually analyze? By annotating LLM–user interaction data, we can ask deeper questions about how people and models communicate.

### LLM-User Interaction Can Be Unsafe

AI safety is trending everywhere—from news coverage to policy debates. In this project, we had an LLM review each user–model exchange and label it “safe” or “unsafe” in ten different risk categories:

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
<br>

### Why LLM Safety Evaluation Is Challenging
* Safety is **Subjective**: Perceptions of "safe" vary by person and culture, leading to conflicting views. Many outputs fall into a gray zone, neither clearly safe nor harmful.

* **No Ground Truth**: Unlike simple tasks (e.g., identifying a dog in a photo, detecting spam emails), safety has no fixed answer, with even experts disagreeing.
<br>
