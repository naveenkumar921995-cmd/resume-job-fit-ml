import streamlit as st
import traceback
from core.resume_parser import parse_resume
from core.feature_engineering import extract_experience_years
from core.job_roles import get_job_role_keywords

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------
st.set_page_config(
    page_title="Resume Job Fit Analyzer",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------------
# CUSTOM CSS (SaaS Style UI)
# ----------------------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.stButton>button {
    background: linear-gradient(90deg,#4CAF50,#00C9A7);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #1E222A;
    margin-top: 15px;
}
.score-high {color: #00FFAA; font-size: 28px; font-weight: bold;}
.score-medium {color: #FFC107; font-size: 28px; font-weight: bold;}
.score-low {color: #FF4B4B; font-size: 28px; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# HEADER
# ----------------------------------------
st.title("📄 Resume Job Fit Analyzer")
st.markdown("### AI-powered Resume Matching System")

# ----------------------------------------
# SIDEBAR
# ----------------------------------------
st.sidebar.header("🔎 Job Selection")

job_role = st.sidebar.selectbox(
    "Select Job Role",
    [
        "Data Scientist",
        "Cybersecurity",
        "Cloud DevOps",
        "Product Manager",
        "Marketing",
        "Finance",
        "Healthcare",
        "HR",
        "Legal",
        "Operations",
        "Design"
    ]
)

# ----------------------------------------
# FILE UPLOAD
# ----------------------------------------
uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

# ----------------------------------------
# SCORING FUNCTION
# ----------------------------------------
def calculate_match_score(resume_text, job_role):
    role_keywords = get_job_role_keywords(job_role)
    resume_text_lower = resume_text.lower()

    matched = 0
    for keyword in role_keywords:
        if keyword.lower() in resume_text_lower:
            matched += 1

    score = int((matched / len(role_keywords)) * 100) if role_keywords else 0
    return score

# ----------------------------------------
# MAIN PROCESS
# ----------------------------------------
if uploaded_file:

    try:
        resume_text = parse_resume(uploaded_file)
        experience_years = extract_experience_years(resume_text)
        match_score = calculate_match_score(resume_text, job_role)

        st.markdown("---")
        st.subheader("📊 Analysis Results")

        # SCORE DISPLAY
        if match_score >= 75:
            score_class = "score-high"
        elif match_score >= 45:
            score_class = "score-medium"
        else:
            score_class = "score-low"

        st.markdown(f"""
        <div class="result-box">
            <div>🎯 Job Match Score</div>
            <div class="{score_class}">{match_score}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
            <div>🕒 Estimated Experience</div>
            <div style="font-size:22px;">{experience_years} Years</div>
        </div>
        """, unsafe_allow_html=True)

        # RECOMMENDATION
        st.markdown("### 📌 Recommendation")

        if match_score >= 75:
            st.success("Strong match! You are highly aligned with this role.")
        elif match_score >= 45:
            st.warning("Moderate match. Consider improving skill alignment.")
        else:
            st.error("Low match. Resume needs optimization for this role.")

        # EXPANDABLE RAW TEXT
        with st.expander("🔍 View Extracted Resume Text"):
            st.write(resume_text)

    except Exception as e:
        st.error("An error occurred while processing the resume.")
        st.code(traceback.format_exc())

# ----------------------------------------
# FOOTER
# ----------------------------------------
st.markdown("---")
st.markdown("© 2026 Resume Job Fit ML | Built with Streamlit")
