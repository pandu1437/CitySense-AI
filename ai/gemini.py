import streamlit as st
import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(question, df):

    prompt = f"""
You are a senior data analyst.

Dataset:
{df.head(50).to_string()}

Question:
{question}

Give:
- Summary
- Key insights
- Recommendation
"""

    response = model.generate_content(prompt)
    return response.text