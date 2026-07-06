import os
from dotenv import load_dotenv
from google import genai

import streamlit as st

API_KEY = st.secrets["GEMINI_API_KEY"]

print("=" * 50)
print("Gemini.py Loaded")
print("API Key Found:", API_KEY is not None)

client = genai.Client(api_key=API_KEY)


def ask_gemini(question, df):

    prompt = f"""
Dataset Columns:
{list(df.columns)}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text