# AI-Powered Resume Analyzer & Career Recommendation System

## Overview

An end-to-end Machine Learning and NLP application that analyzes PDF resumes and predicts the most suitable job role based on resume content.

The system extracts technical skills, calculates a resume score, identifies missing skills, and provides personalized recommendations through an interactive Streamlit dashboard.

---

## Features

* Upload Resume in PDF format
* Extract text from PDF resumes
* Predict job role using Machine Learning
* Extract technical skills automatically
* Calculate Resume Score
* Identify Missing Skills
* Interactive Streamlit Dashboard

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* TF-IDF Vectorization
* Logistic Regression
* Streamlit
* PDFPlumber

---

## Machine Learning Pipeline

Resume PDF
→ Text Extraction
→ Text Preprocessing
→ TF-IDF Vectorization
→ Logistic Regression Model
→ Job Role Prediction
→ Skill Extraction
→ Resume Scoring
→ Skill Gap Analysis

---

## Project Structure

resume-analyzer/

├── app.py

├── requirements.txt

├── README.md

├── data/

│ └── UpdatedResumeDataSet.csv

├── models/

│ ├── resume_classifier.pkl

│ ├── tfidf_vectorizer.pkl

│ └── label_encoder.pkl

└── src/

├── predictor.py

├── skill_extractor.py

├── resume_scorer.py

├── pdf_utils.py

└── **init**.py

---

## Model Information

Algorithm: Logistic Regression

Feature Engineering: TF-IDF Vectorization

Model Accuracy: 99.48%

---

## Installation

Clone the repository:

git clone <your-github-repo-url>

cd resume-analyzer

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Future Improvements

* Deep Learning based Resume Classification
* Resume Ranking System
* Job Recommendation Engine
* Resume ATS Score Analysis
* Cloud Deployment

---

## Author

Amrit Pandey

B.Tech CSE Student

Interested in Machine Learning, Data Science and AI
