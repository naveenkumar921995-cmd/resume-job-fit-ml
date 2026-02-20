import streamlit as st
import traceback
from core.resume_parser import parse_resume
from core.feature_engineering import extract_experience_years
from core.job_roles import get_job_data

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------
st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="🚀",
    layout="wide"
)

# ----------------------------------------
# CUSTOM UI
# ----------------------------------------
st.markdown("""
<style>
.metric-card {
    padding:20px;
    border-radius:15px;
    background:#1E222A;
    text-align:center;
}
.big-score {
    font-size:40px;
    font-weight:bold;
}
.good {color:#00FFAA;}
.mid {color:#FFC107;}
.bad {color:#FF4B4B;}
</style>
""", unsafe_allow_html=True)

st.title("🚀 AI Resume Job Match System")

# ----------------------------------------
# LOAD JOB DATA
# ----------------------------------------
job_data = get_job_data()

# ----------------------------------------
# SIDEBAR SELECTION
# ----------------------------------------
st.sidebar.header("📌 Job Selection")

department = st.sidebar.selectbox(
    "Select Department",
    list(job_data.keys())
)

job_post = st.sidebar.selectbox(
    "Select Job Role",
    list(job_data[department].keys())
)

required_skills = job_data[department][job_post]

# ----------------------------------------
# FILE UPLOAD
# ----------------------------------------
uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

# ----------------------------------------
# SCORING ENGINE
# ----------------------------------------
def calculate_score(resume_text, skills):
    resume_text_lower = resume_text.lower()

    matched = []
    missing = []

    for skill in skills:
        if skill.lower() in resume_text_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(skills)) * 100)

    return score, matched, missing

# ----------------------------------------
# MAIN PROCESS
# ----------------------------------------
if uploaded_file:

    try:
        resume_text = parse_resume(uploaded_file)
        experience_years = extract_experience_years(resume_text)

        score, matched_skills, missing_skills = calculate_score(
            resume_text,
            required_skills
        )

        st.markdown("---")
        st.subheader("📊 Match Results")

        col1, col2 = st.columns(2)

        with col1:
            score_class = "good" if score >= 75 else "mid" if score >= 45 else "bad"

            st.markdown(f"""
            <div class="metric-card">
                <div>🎯 Match Score</div>
                <div class="big-score {score_class}">{score}%</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div>🕒 Experience</div>
                <div class="big-score">{experience_years} Years</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")
            for skill in matched_skills:
                st.success(skill)

        with col4:
            st.subheader("❌ Missing Skills")
            for skill in missing_skills:
                st.error(skill)

        st.markdown("---")

        if score >= 75:
            st.success("🔥 Strong Candidate for this role!")
        elif score >= 45:
            st.warning("⚡ Moderate Fit — Improve Missing Skills")
        else:
            st.error("🚨 Low Match — Resume Needs Optimization")

        with st.expander("📄 View Resume Text"):
            st.write(resume_text)

    except Exception:
        st.error("Error processing resume")
        st.code(traceback.format_exc())

# ----------------------------------------
# FOOTER
# ----------------------------------------
st.markdown("---")
st.markdown("© 2026 AI Resume Matcher | SaaS Edition")
