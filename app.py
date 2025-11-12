import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from model.recommender import CareerRecommender

# Load environment variables
load_dotenv()

# ✅ Load career dataset
career_data = pd.read_csv("data/careers.csv")

# ✅ Initialize the recommender with data
recommender = CareerRecommender(career_data)

# ==============================
# 🎨 Streamlit Setup
# ==============================
st.set_page_config(page_title="CareerCompass", page_icon="🧭")
st.title("🧭 CareerCompass — Intelligent Career Chatbot")

st.markdown(
    """
    Hi! I’m your AI-powered career assistant. 💡   
    Describe your **interests** to get personalized career recommendations.
    """
)

# ==============================
# 💬 Chat Section
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==============================
# 🧠 Input Box
# ==============================
st.markdown("### 💬 Tell me about your interests:")
prompt = st.chat_input("e.g., I love solving problems and working with data")

if prompt:
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Step 1 — Get top career matches
    try:
        recommendations = recommender.recommend(prompt, top_n=5)
    except Exception as e:
        recommendations = None
        reply = f"⚠️ Error fetching recommendations: {e}"
    else:
        # Step 2 — Build the final response
        reply = "📋 **Top Career Recommendations:**"
        if recommendations is not None and not recommendations.empty:
            for _, row in recommendations.iterrows():
                reply += (
                    f"\n\n🎯 **{row['job_role']}** — {row['description']}"
                    f"\n🧩 *Skills Required:* {row['required_skills']}"
                )
        else:
            reply += "\n\n(No recommendations available right now.)"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})