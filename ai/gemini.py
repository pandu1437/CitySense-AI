import streamlit as st
from google import genai

API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

def ask_gemini(question, df):

    prompt = f"""
You are a Senior Data Analyst AI.

Dataset:
{df.head(50).to_string()}

Question:
{question}

Give:
- Summary
- Key insights
- Recommendations
"""

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=prompt
    )

    return response.text