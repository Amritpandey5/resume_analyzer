import joblib
from skill_extractor import extract_skills
from resume_scorer import calculate_score, get_missing_skills

model = joblib.load("models/resume_classifier.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")