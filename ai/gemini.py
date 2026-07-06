import streamlit as st
import google.generativeai as genai

# ----------------------------
# SAFE API KEY LOADING
# ----------------------------
API_KEY = st.secrets.get("GEMINI_API_KEY", None)

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in Streamlit secrets")

genai.configure(api_key=API_KEY)

# ----------------------------
# USE WORKING MODEL
# ----------------------------
model = genai.GenerativeModel("gemini-1.5-pro ✅")

# ----------------------------
# MAIN FUNCTION
# ----------------------------
def ask_gemini(question, df):

    prompt = f"""
You are a Senior Data Analyst AI.

Analyze the dataset and give structured insights.

Dataset (sample):
{df.head(50).to_string()}

Question:
{question}

Respond in:
- Short answer
- Key insights
- Recommendation
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error from Gemini: {str(e)}"