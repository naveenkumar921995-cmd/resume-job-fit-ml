import streamlit as st
from core.similarity_engine import semantic_similarity
from core.feature_engineering import extract_experience_years, keyword_density
from core.prediction import predict_fit
from core.genai_engine import generate_feedback

st.set_page_config(page_title="Resume-Job Fit ML System", layout="wide")

st.title("🚀 Resume–Job Fit Prediction System")

resume_text = st.text_area("Paste Resume Text")
job_text = st.text_area("Paste Job Description")

if resume_text and job_text:

    semantic_score = semantic_similarity(resume_text, job_text)
    exp_years = extract_experience_years(resume_text)
    keyword_score = keyword_density(resume_text, job_text)

    skill_match = keyword_score  # simplified mapping

    fit_score = predict_fit(skill_match, semantic_score,
                            keyword_score, exp_years)

    feedback = generate_feedback(fit_score)

    st.subheader("📊 Prediction Results")

    col1, col2 = st.columns(2)
    col1.metric("Predicted Fit Score", f"{fit_score}/100")
    col2.metric("Semantic Similarity", f"{semantic_score}%")

    st.progress(fit_score / 100)

    st.subheader("🤖 AI Feedback")
    st.success(feedback)
