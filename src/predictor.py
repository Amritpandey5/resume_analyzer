import joblib

from src.skill_extractor import extract_skills
from src.resume_scorer import calculate_score, get_missing_skills

# Load saved models
model = joblib.load("models/resume_classifier.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


def predict_resume(resume_text):

    # Extract skills
    skills = extract_skills(resume_text)

    # Transform text
    vector = tfidf.transform([resume_text])

    # Predict role
    prediction = model.predict(vector)
    role = label_encoder.inverse_transform(prediction)[0]

    # Calculate score
    score = calculate_score(skills)

    # Missing skills
    missing_skills = get_missing_skills(role, skills)

    return {
        "role": role,
        "skills": skills,
        "score": score,
        "missing_skills": missing_skills
    }


if __name__ == "__main__":

    sample_resume = """
    Python
    Pandas
    NumPy
    Machine Learning
    TensorFlow
    Git
    AWS
    """

    result = predict_resume(sample_resume)

    print("\nPredicted Role:", result["role"])
    print("\nDetected Skills:", result["skills"])
    print("\nResume Score:", result["score"])
    print("\nMissing Skills:", result["missing_skills"])