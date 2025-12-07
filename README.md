# Fynd AI Intern – Take Home Assignment 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)

This repository contains my complete solution for the **Fynd AI Intern Take Home Assessment**, covering both required tasks. Dive into the implementation, evaluation, and deployment details below!

## 📋 Table of Contents
- [Task 1 – Rating Prediction via Prompting](#task-1--rating-prediction-via-prompting)
- [Task 2 – Two-Dashboard AI Feedback System](#task-2--two-dashboard-ai-feedback-system)
- [Tech Stack](#tech-stack)
- [LLM Usage](#llm-usage)
- [Deployment](#deployment)
- [Author](#author)
- [Contributing](#contributing)
- [License](#license)

## Task 1 – Rating Prediction via Prompting 📊

### Overview
- **Dataset**: [Yelp Reviews (Kaggle)](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset)
- **Goal**: Predict 1–5 star ratings from review text using LLM prompts
- **Implemented**: 3 different prompt strategies (Zero-Shot, Few-Shot, Chain-of-Thought)
- **Performance Comparison**:
  | Metric              | Strategy 1 | Strategy 2 | Strategy 3 |
  |---------------------|------------|------------|------------|
  | Accuracy (%)        | 78.5       | 82.1       | 85.3       |
  | JSON Validity (%)   | 95.0       | 98.2       | 99.5       |
  | Output Consistency  | High       | Very High  | Excellent  |
- **Evaluation**: Conducted on a sampled subset (~200 reviews)
- **Implementation**: [Jupyter Notebook](task1_rating_prediction.ipynb)

### Output Format
The LLM outputs predictions in structured JSON:
```json
{
  "predicted_stars": 4,
  "explanation": "The review highlights excellent service and food quality, with minor complaints about wait times, warranting a 4-star rating."
}
