import streamlit as st

from src.pdf_utils import extract_text_from_pdf
from src.predictor import predict_resume

st.set_page_config(
    page_title="Resume Analyzer",
    layout="wide"
)

st.title("📄 Resume Analyzer & Job Recommendation System")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    result = predict_resume(resume_text)

    st.subheader("🎯 Predicted Role")
    st.success(result["role"])

    st.subheader("📊 Resume Score")
    st.progress(result["score"] / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Predicted Role", result["role"])

    with col2:
        st.metric("Resume Score", f"{result['score']}/100")

    st.subheader("🛠 Detected Skills")

    for skill in result["skills"]:
        st.badge(skill)
    st.subheader("📈 Recommended Skills")

    for skill in result["missing_skills"]:
        st.write(f"🔹 {skill}") 

else:
    st.info("Upload a PDF resume to start analysis.")