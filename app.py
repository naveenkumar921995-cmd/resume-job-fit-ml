import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from core.job_roles import JOB_ROLES
from core.resume_parser import parse_resume
from core.feature_engineering import extract_experience_years

st.set_page_config(page_title="Resume Job Fit Analyzer")

st.title("📊 AI Resume Job Fit Analyzer")

# 1️⃣ Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# 2️⃣ Department Selection
department = st.selectbox("Select Department", list(JOB_ROLES.keys()))

# 3️⃣ Role Selection
role = st.selectbox("Select Job Role", list(JOB_ROLES[department].keys()))

if uploaded_file:
    resume_text = parse_resume(uploaded_file)

    if st.button("Analyze Fit"):
        required_skills = JOB_ROLES[department][role]

        resume_text_lower = resume_text.lower()

        matched_skills = [skill for skill in required_skills if skill in resume_text_lower]
        missing_skills = [skill for skill in required_skills if skill not in resume_text_lower]

        experience_years = extract_experience_years(resume_text)

        score = int((len(matched_skills) / len(required_skills)) * 100)

        st.subheader("📈 Fit Score")
        st.progress(score)
        st.write(f"**Score:** {score}%")

        st.subheader("🧠 Experience Detected")
        st.write(f"{experience_years} Years")

        st.subheader("✅ Matching Skills")
        st.write(matched_skills)

        st.subheader("❌ Missing Skills")
        st.write(missing_skills)

        if score >= 70:
            st.success("Strong Fit ✅")
        elif score >= 40:
            st.warning("Moderate Fit ⚠️")
        else:
            st.error("Low Fit ❌")
