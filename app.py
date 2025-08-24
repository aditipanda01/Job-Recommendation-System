import streamlit as st
import pandas as pd
import pickle

# ---- LOAD DATA ----
df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# ---- RECOMMENDATION FUNCTION ----
def recommendation(title):
    idx = df[df['Title']==title].index[0]
    idx = df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)
    return jobs

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="💼",
    layout="centered"
)

# ---- CSS FOR ANIMATED BACKGROUND (modern soft colors) ----
st.markdown(
    """
    <style>
    /* Animated Gradient Background */
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #dbeafe, #ede9fe, #fff1f2, #fef9c3);
        background-size: 400% 400%;
        animation: gradientMove 18s ease infinite;
    }

    /* Content overlay (glass effect) */
    .content {
        position: relative;
        z-index: 1;
        padding: 40px;
        text-align: center;
        color: #1e293b;
        backdrop-filter: blur(12px);
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.6);
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        max-width: 650px;
        margin: auto;
    }

    h1, h2, label {
        color: #1e293b;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1, #3b82f6);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- APP CONTENT ----
st.markdown('<div class="content">', unsafe_allow_html=True)
st.title('💼 Job Recommendation System')

# Input
title = st.selectbox('Search job', df['Title'])

# Show recommendations only after button click
if st.button("🔍 Get Recommendations"):
    jobs = recommendation(title)
    if jobs:
        st.subheader("Here are some recommended jobs for you:")
        for idx, job in enumerate(jobs, start=1):
            st.write(f"{idx}. {job}")

st.markdown('</div>', unsafe_allow_html=True)
