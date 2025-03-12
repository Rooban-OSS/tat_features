import streamlit as st

# Page Config
st.set_page_config(page_title="AI Hiring Platform Roadmap", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #1E1E2E;
            color: #F8F9FA;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            padding: 10px 0;
            color: #FFD700;
        }
        .subtitle {
            font-size: 22px;
            text-align: center;
            font-weight: 500;
            color: #BBB;
            margin-bottom: 15px;
        }
        .highlight-box {
            background: #27293D;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 15px rgba(255, 215, 0, 0.2);
        }
        .section-title {
            font-size: 26px;
            font-weight: bold;
            margin: 10px 0;
            color: #FFD700;
        }
        .feature-list {
            font-size: 18px;
            padding: 5px;
            margin-left: 15px;
            color: #F8F9FA;
        }
        .divider {
            border-top: 2px solid #FFD700;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Introduction
st.markdown("<div class='title'>🚀 AI Hiring Platform Roadmap</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>From AI-based Hiring to Predictive Analytics – Explore Our Evolution</div>", unsafe_allow_html=True)

# Featured Highlights (Key Points at the Top)
st.markdown("### 🌟 **Key Highlights**")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='highlight-box'><b>✅ AI-Powered Hiring</b><br>AI Agents, Resume Matchmaking, Video Interviews</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='highlight-box'><b>✅ Next-Gen Assessments</b><br>Coding Challenges, MCQs, Proctoring & Voice Agents</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='highlight-box'><b>✅ Job Intelligence</b><br>Job Aggregator, Career Roadmap, AI Chatbot</div>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Roadmap Data
phases = {
    "🚀 Phase 2 (Feb - April)": [
        "**Round 1:** AI & Custom MCQs (Critical Thinking, Logic, Psychometrics)",
        "**Round 2:** MERN Stack Coding Assessments",
        "**Round 3:** AI-Human Video Interviews + Speech-to-Text",
        "**Job Intelligence:** FAANG, Big 7 Job Aggregator, Career Path Guide",
        "**Proctoring System:** Custom AI Proctoring for Assessments",
        "**Resume Matchmaker AI** & GDPR/SOC Compliance",
        "**Community:** WhatsApp, Discord, YouTube for Hiring Insights",
        "**One-Click Interview Invites** & Multi-Format Report Downloads"
    ],
    "🔥 Phase 3 (April - July)": [
        "**Round 1:** Advanced Tech Assessments (Cloud, AIML, DSA)",
        "**Round 2:** AI-Driven Coding Tests & Mock Interviews",
        "**Round 3:** AI Video Interview Bot",
        "**Online Hackathon Platform** - Fully Automated Hackathons",
        "**User Social Profiling:** Resume Auto-Update, GitHub & LinkedIn Sync",
        "**AI Voice Agents** - Candidate Screening & Scheduling",
        "**Smart ATS** with Enhanced One-Click Hiring"
    ],
    "⚡ Phase 4 (July - Sept)": [
        "**Game-Based Hiring Assessments** for Fun & Insightful Hiring",
        "**Campus Hiring Tools** - AI-Driven University Recruitment",
        "**Predictive Analytics** - AI to Forecast Candidate Success",
        "**Mobile Optimization** - Enhanced UX for Mobile Assessments",
        "**Full PostgreSQL & Next.js Migration** for Scalability"
    ]
}

# Display Roadmap with Collapsible Sections
for phase, features in phases.items():
    with st.expander(phase, expanded=False):
        for feature in features:
            st.markdown(f"<div class='feature-list'>• {feature}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
