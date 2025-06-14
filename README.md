# LLMs are Overtaking Traditional NLP Methods

Unstructured text—such as search queries, social media posts, and free-form responses—poses significant challenges for traditional analytical methods:

* Dictionary-Based Approaches often fail to capture the full spectrum of linguistic variation, as users express the same concept in multiple ways.
* Supervised Machine Learning requires extensive labeled data and contextual metadata, which are typically unavailable for ad-hoc text streams and infrequent query types.
 
Large language models (LLMs) are rapidly emerging as a compelling alternative!

* They understand subtle nuances in text so can classify on a more granular level
* they can classify based on criteria subjective in nature where no ground truth exists

## A. Text Classification Feasible with Traditional Tools
* **Sentiment Analysis**
"Label customer reviews as positive or negative"

* **Spam Detection**
"Flag incoming emails containing blacklisted URLs"

## B. Text Classification Only Practical with LLMs
* **Churn-Risk Signal**
"Classify customer message into risk archetypes (e.g., switching for cost reasons, hate UI)"

* **Granular Intent Classification**
"Determine whether a customer message is asking for a **refund**, **technical help**, etc"

* **Review Helpfulness**
"Read this customer review and tag it as **helpful**, **neutral**, or **unhelpful**"

* **Hallucination Detection**
"Does this response assert any facts not in the source doc?"
<br><br>

# Research Applications of LLMs

Empirical studies demonstrate that LLM outputs align closely with human raters across a range of annotation tasks [(Bail, 2024)](https://www.pnas.org/doi/10.1073/pnas.2314021121)
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

# Best Practices & Tips

> **Use Fully-Specified Checklists**
- Underspecified rubrics lead to lower inter-annotator agreement and higher subjective variance
- Define every criterion in precise, unambiguous terms
- Present the LLM with a literal "check the boxes" rubric

> **Favor Binary Judgments Over Likert Scales**
- Defining distinct, objective criteria for each point on a 1-5 scale can be surprisingly difficult
- Forcing binary decisions produces more reproducible annotations

> **Break Complex Tasks into Small, Binary Tasks ("Divide and Conquer" Approach)**
- Example for tone evaluation: (1) Does the text use any profanity? (2) Is the greeting present ("Hello", "Hi")? (3) Are please and thank you included?

> **Prefer Pairwise or Ranking Prompts**
- Ask the LLM "Which of the two responses is more accurate" instead of "Rate this response 1-5"

> **Guard Against LLM Biases**
- Position Bias
- Verbosity Bias
- Self-enhancement Bias

> **Match Tasks to the Model's Strengths**
- Leverage LLMs for judgments they have seen during pre-training
- For highly specificalized domains, provide extrac context or domain examples
<br><br>

# Ensuring Validity of Your LLM tool
<br><br>

# Next Steps & Further Reading
* Prompt Engineering:
* LLM Evaluation Literature


# Citation
While the original paper outlines the algorithm, the Large Language Model prompts in this repository (see template_rainbow.py) are my original contributions.
If you find the LLM prompts from this repository useful, please cite it with:
@misc{???,
  author = {Juwon Hong},
  title = {'???'},
  year = {2025},
  url = {https://github.com/jean-jsj/???}
}