import streamlit as st
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
import random

# ----------------- Streamlit Page Config ------------------


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, .stApp {
    font-family: 'Poppins', sans-serif;
    background: transparent !important;
}

body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    width: 100vw;
    height: 100vh;
    background: linear-gradient(-45deg, #dbeafe, #93c5fd, #bfdbfe, #eff6ff);
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
    opacity: 0.9;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background-color: rgba(255, 255, 255, 0.75);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem auto;
    max-width: 1000px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.stButton > button {
    background-color: #1d4ed8;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 0.6em 1.6em;
    transition: 0.2s ease;
}
.stButton > button:hover {
    background-color: #2563eb;
}

.highlight-box {
    background: #ffffff;
    border-left: 6px solid #3b82f6;
    padding: 1.2rem;
    margin: 1rem 0;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)


# ----------------- App Title ------------------
st.markdown("""
    <div style="text-align:center">
        <h1 style="color:#1d4ed8">CareerLens AI 🔍</h1>
        <p>Smart AI Resume Analyzer + Career Alternative Recommender</p>
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="100" style="margin-top:10px;">
    </div>
""", unsafe_allow_html=True)

# ----------------- Upload Resume ------------------
st.subheader("📄 Upload Your Resume")
uploaded_file = st.file_uploader("Choose your resume (PDF only)", type="pdf")

# ----------------- Role-Skill Database ------------------
roles_db = {
    "Data Scientist": ["python", "pandas", "machine learning", "data analysis", "statistics"],
    "AI Engineer": ["deep learning", "tensorflow", "pytorch", "neural networks", "nlp"],
    "Web Developer": ["html", "css", "javascript", "react", "frontend", "backend"],
    "Data Analyst": ["sql", "excel", "power bi", "tableau", "visualization"],
    "Software Developer": ["java", "c++", "git", "system design", "algorithms"],
    "Business Analyst": ["communication", "presentation", "research", "stakeholders", "analytics"],
    "Cybersecurity Analyst": ["network", "security", "vulnerability", "firewall", "risk"]
}

# ----------------- Extract PDF Text ------------------
def extract_text(file):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    text = " ".join([page.get_text() for page in pdf])
    return text.lower()

# ----------------- Recommend Careers ------------------
def recommend_roles(text):
    matches = defaultdict(int)
    for role, keywords in roles_db.items():
        for kw in keywords:
            if kw in text:
                matches[role] += 1
    sorted_roles = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    return sorted_roles[:3]

# ----------------- Generate Explanation ------------------
def explain_reason(role, text):
    found = [kw for kw in roles_db[role] if kw in text]
    if not found:
        return f"We suggest exploring the {role} role as a new career path that could align with your potential skills and learning curve."
    reason_starts = [
        "Your experience in",
        "You've clearly worked with",
        "Skills like",
        "We noticed keywords like"
    ]
    start = random.choice(reason_starts)
    return f"{start} {', '.join(found)} suggest you are well-suited for a {role} position."

# ----------------- Main Logic ------------------
if uploaded_file:
    st.markdown("---")
    st.subheader(" AI Analysis & Suggestions")
    with st.spinner("Analyzing resume with AI..."):
        resume_text = extract_text(uploaded_file)
        top_roles = recommend_roles(resume_text)

    for role, score in top_roles:
        reason = explain_reason(role, resume_text)
        st.markdown(f"""
            <div class='highlight-box'>
                <h4 style='color:#1d4ed8'>{role}</h4>
                <p><strong>Match Score:</strong> {score}</p>
                <p>{reason}</p>
            </div>
        """, unsafe_allow_html=True)

    st.success(" Analysis Complete!!!!")
