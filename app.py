import streamlit as st
import re
import pdfplumber
import docx

from core.job_roles import get_job_data


# ---------------------------
# Resume Text Extraction
# ---------------------------

def extract_text(uploaded_file):
    text = ""

    if uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text.lower()


# ---------------------------
# Match Score Calculation
# ---------------------------

def calculate_match(resume_text, keywords):
    matched = []

    for skill in keywords:
        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", resume_text):
            matched.append(skill)

    if len(keywords) == 0:
        return 0, [], keywords

    score = int((len(matched) / len(keywords)) * 100)
    missing = list(set(keywords) - set(matched))

    return score, matched, missing


# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="Resume Job Fit Analyzer", layout="wide")

st.title("📄 AI Resume Job Fit Analyzer")
st.markdown("Match your resume against real industry job roles.")


# ---------------------------
# Job Selection
# ---------------------------

job_data = get_job_data()

department = st.selectbox(
    "Select Department",
    list(job_data.keys())
)

job_role = st.selectbox(
    "Select Job Role",
    list(job_data[department].keys())
)

keywords = job_data[department][job_role]


# ---------------------------
# Resume Upload
# ---------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    if resume_text.strip() == "":
        st.error("Could not extract text from resume.")
    else:

        score, matched_skills, missing_skills = calculate_match(
            resume_text,
            keywords
        )

        st.subheader("📊 Match Score")
        st.progress(score / 100)
        st.success(f"Overall Match: {score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            if matched_skills:
                for skill in matched_skills:
                    st.write(f"- {skill}")
            else:
                st.write("No skills matched.")

        with col2:
            st.subheader("❌ Missing Skills")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"- {skill}")
            else:
                st.write("No missing skills. Great fit!")

        st.subheader("📌 Required Skills for Role")
        for skill in keywords:
            st.write(f"- {skill}")
