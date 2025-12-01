"""Prompt for Glossary of AI Terms."""

PROMPT = """
# Task: Generate Glossary of AI Terms

Create a comprehensive glossary of AI and technology terms relevant to {company_name}'s AI journey.

## Required Sections

### 1. Introduction

This glossary provides definitions for key terms related to artificial intelligence, machine learning, and data technologies. It is designed to help all team members at {company_name} communicate effectively about AI initiatives.

---

### 2. Core AI Concepts

#### A

**Agentic AI**
AI systems capable of autonomous action and decision-making without constant human intervention. These systems can plan, execute, and adjust strategies to achieve goals.

**Artificial General Intelligence (AGI)**
Hypothetical AI with human-level reasoning and problem-solving across any domain. Current AI systems are "narrow" AI, excelling at specific tasks.

**Artificial Intelligence (AI)**
Computer systems designed to perform tasks typically requiring human intelligence, including visual perception, speech recognition, decision-making, and language translation.

#### B

**Bias (in AI)**
Systematic errors in AI outputs that reflect prejudices in training data or algorithm design. Can lead to unfair outcomes for certain groups.

#### C

**Chatbot**
Software application that simulates human conversation through text or voice interactions. Modern chatbots often use large language models.

**Computer Vision**
AI capability to interpret and understand visual information from images or videos, enabling tasks like object detection and facial recognition.

#### D

**Data Lake**
Centralized repository storing raw data in its native format until needed for analysis. Enables flexible data exploration and AI training.

**Deep Learning**
Subset of machine learning using neural networks with multiple layers. Powers advanced AI capabilities like image recognition and language understanding.

#### E

**Embeddings**
Numerical representations of text, images, or other data that capture semantic meaning. Enables AI to find similarities and relationships.

#### F

**Fine-tuning**
Process of adapting a pre-trained AI model for a specific task or domain by training it on additional relevant data.

**Foundation Model**
Large AI model trained on broad data that can be adapted for various tasks. Examples: GPT-4, Claude, Gemini.

#### G

**Generative AI**
AI systems that create new content (text, images, code, audio) based on learned patterns. The technology behind ChatGPT and similar tools.

**GPT (Generative Pre-trained Transformer)**
Architecture powering many large language models. Pre-trained on vast text data, then fine-tuned for specific applications.

#### H

**Hallucination**
When AI generates plausible-sounding but false or fabricated information. Important consideration for all generative AI applications.

#### I

**Inference**
The process of using a trained AI model to make predictions or generate outputs on new data.

#### L

**Large Language Model (LLM)**
AI model trained on massive text datasets to understand and generate human language. Powers chatbots and writing assistants.

#### M

**Machine Learning (ML)**
Subset of AI where systems learn from data to improve performance without explicit programming. Foundation for most modern AI applications.

**Model**
Mathematical representation learned from data that can make predictions or generate outputs. The core component of AI systems.

#### N

**Natural Language Processing (NLP)**
AI capability to understand, interpret, and generate human language. Enables chatbots, translation, and sentiment analysis.

**Neural Network**
Computing system inspired by biological neurons. Learns patterns through interconnected nodes processing information.

#### P

**Prompt**
Input text or instructions given to a generative AI model. Prompt quality significantly affects output quality.

**Prompt Engineering**
The practice of designing effective prompts to get desired outputs from AI models.

#### R

**RAG (Retrieval-Augmented Generation)**
Technique that combines AI text generation with information retrieval from knowledge bases. Reduces hallucinations by grounding responses in real data.

**Reinforcement Learning from Human Feedback (RLHF)**
Training technique using human preferences to improve AI model behavior and alignment with user expectations.

#### S

**Sentiment Analysis**
AI technique to determine emotional tone in text. Used for customer feedback analysis and social media monitoring.

**Supervised Learning**
Machine learning approach using labeled training data. The model learns to map inputs to known outputs.

#### T

**Token**
Unit of text processed by language models. Can be a word, part of a word, or punctuation. Important for understanding AI pricing and limits.

**Training Data**
Dataset used to teach AI models patterns and relationships. Quality and diversity of training data directly impacts model performance.

**Transformer**
Neural network architecture enabling efficient processing of sequential data. Powers modern language models.

#### U

**Unsupervised Learning**
Machine learning approach finding patterns in unlabeled data. Used for clustering, anomaly detection, and data exploration.

#### V

**Vector Database**
Database optimized for storing and searching embeddings. Enables semantic search and AI memory capabilities.

---

### 3. Business & Strategy Terms

**AI Maturity**
Organization's sophistication in adopting and leveraging AI. Measured across dimensions like strategy, data, talent, and governance.

**AI Readiness**
Organization's preparedness to implement AI initiatives. Includes data quality, infrastructure, skills, and culture factors.

**Center of Excellence (CoE)**
Dedicated team providing AI leadership, best practices, and support across an organization.

**Digital Transformation**
Fundamental change in how an organization operates and delivers value through digital technology adoption.

**MLOps**
Practices for deploying and maintaining machine learning models in production reliably and efficiently.

**ROI (Return on Investment)**
Measure of AI initiative profitability. Calculated as (Benefits - Costs) / Costs × 100.

**Total Cost of Ownership (TCO)**
Complete cost of implementing and operating an AI solution over its lifecycle.

---

### 4. Data Terms

**Data Governance**
Framework for managing data availability, usability, integrity, and security across an organization.

**Data Lake**
Storage repository holding vast amounts of raw data in native format.

**Data Pipeline**
Automated process moving and transforming data from sources to destinations.

**Data Quality**
Measure of data accuracy, completeness, consistency, and reliability.

**Data Warehouse**
Central repository of integrated, structured data optimized for analysis.

**ETL (Extract, Transform, Load)**
Process of extracting data from sources, transforming it, and loading into a destination system.

**Metadata**
Data about data - describing structure, origin, quality, and relationships.

---

### 5. Technical Terms

**API (Application Programming Interface)**
Interface enabling different software systems to communicate. How applications integrate with AI services.

**Cloud Computing**
Delivery of computing services over the internet. Major providers: AWS, Azure, Google Cloud.

**Edge Computing**
Processing data near its source rather than in centralized cloud. Enables real-time AI applications.

**GPU (Graphics Processing Unit)**
Hardware accelerating AI model training and inference. Essential for computationally intensive AI workloads.

**Latency**
Time delay between input and response. Critical metric for real-time AI applications.

**SaaS (Software as a Service)**
Cloud-based software delivery model. Most AI tools are delivered as SaaS.

---

### 6. Industry-Specific Terms

[Add terms relevant to {company_name}'s industry]

---

### 7. Acronyms Quick Reference

| Acronym | Full Term |
|---------|-----------|
| AI | Artificial Intelligence |
| AGI | Artificial General Intelligence |
| API | Application Programming Interface |
| CoE | Center of Excellence |
| ETL | Extract, Transform, Load |
| GPU | Graphics Processing Unit |
| LLM | Large Language Model |
| ML | Machine Learning |
| MLOps | Machine Learning Operations |
| NLP | Natural Language Processing |
| RAG | Retrieval-Augmented Generation |
| RLHF | Reinforcement Learning from Human Feedback |
| ROI | Return on Investment |
| SaaS | Software as a Service |
| TCO | Total Cost of Ownership |

## Output Format
- Alphabetical organization
- Clear, non-technical definitions
- Examples where helpful
- Relevance to business context
- Include industry-specific terms
"""
