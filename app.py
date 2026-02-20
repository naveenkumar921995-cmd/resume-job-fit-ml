import streamlit as st
import re
import pdfplumber
import docx
import matplotlib.pyplot as plt

from core.job_roles import get_job_data


# ---------------------------
# Page Config (MUST BE FIRST STREAMLIT COMMAND)
# ---------------------------

st.set_page_config(
    page_title="Integrated Department Resume Analyzer",
    layout="wide",
    page_icon="📊"
)


# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("About This System")
st.sidebar.info(
    """
    Integrated Department Resume Analyzer
    
    ✔ Cross-Industry Resume Evaluation  
    ✔ Department-Wise Role Matching  
    ✔ Skill Gap Identification  
    ✔ Keyword-Based ATS Scoring
    """
)


# ---------------------------
# Header Section
# ---------------------------

st.title("📊 Integrated Department Resume Analyzer")

st.markdown(
    """
    ### Multi-Department • Multi-Role • Keyword-Based Resume Evaluation
    
    Analyze resume compatibility across various departments and job roles 
    using structured skill-based matching logic.
    """
)


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
        return 0, [], []

    score = int((len(matched) / len(keywords)) * 100)
    missing = list(set(keywords) - set(matched))

    return score, matched, missing


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

        # ---------------------------
        # Match Score Section
        # ---------------------------

        st.subheader("📊 Match Score")
        st.progress(score / 100)
        st.success(f"Overall Match: {score}%")

        # ---------------------------
        # Score Visualization Chart
        # ---------------------------

        st.subheader("📈 Match Score Visualization")

        fig1, ax1 = plt.subplots()
        ax1.bar(["Match Score"], [score])
        ax1.set_ylim(0, 100)
        ax1.set_ylabel("Percentage")
        ax1.set_title("Resume Compatibility Score")

        st.pyplot(fig1)

        # ---------------------------
        # Matched vs Missing Chart
        # ---------------------------

        st.subheader("📊 Matched vs Missing Skills Comparison")

        matched_count = len(matched_skills)
        missing_count = len(missing_skills)

        fig2, ax2 = plt.subplots()
        ax2.bar(
            ["Matched Skills", "Missing Skills"],
            [matched_count, missing_count]
        )
        ax2.set_ylabel("Number of Skills")
        ax2.set_title("Skill Comparison Analysis")

        st.pyplot(fig2)

        # ---------------------------
        # Skills Breakdown
        # ---------------------------

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

        # ---------------------------
        # Required Skills
        # ---------------------------

        st.subheader("📌 Required Skills for Selected Role")
        for skill in keywords:
            st.write(f"- {skill}")
