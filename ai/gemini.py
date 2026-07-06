import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def ask_gemini(question, df):
    prompt = f"""
You are a senior data analyst.

Dataset:
{df.head(50).to_string()}

Question:
{question}

Provide:
1. Summary
2. Key Insights
3. Recommendations
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text