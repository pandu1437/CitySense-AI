import pandas as pd
from ai.gemini import ask_gemini

df = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Hyderabad"],
    "AQI": [320, 180, 90]
})

print(
    ask_gemini(
        "Which city has the worst air quality?",
        df
    )
)