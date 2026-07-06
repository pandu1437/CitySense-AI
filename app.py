import streamlit as st
import pandas as pd

from analytics.cleaning import clean_data
from analytics.forecasting import forecast_aqi
from analytics.anomaly import detect_anomalies
from analytics.decision import generate_decision_report
from dashboard.charts import show_dashboard
from ai.gemini import ask_gemini

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="CitySense AI",
    page_icon="🌍",
    layout="wide"
)
# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

.main {
    background-color:#F8FAFC;
}

h1{
    color:#1E3A8A;
    font-weight:700;
}

h2,h3{
    color:#2563EB;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:18px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
}

.stButton>button{
    width:100%;
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    padding:10px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1E40AF;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#F1F5F9;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SESSION STATE
# ======================================================

if "df" not in st.session_state:
    st.session_state.df = None

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("🌍 CitySense AI")

st.sidebar.caption(
    "AI-Powered Decision Intelligence Platform"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📂 Upload Dataset",
        "📊 Dashboard",
        "🤖 AI Assistant",
        "📈 Forecast",
        "🚨 Anomaly Detection",
        "🧠 Decision Intelligence",
        "ℹ️ About"
    ]
)

# ======================================================
# HOME
# ======================================================

if page == "🏠 Home":

    st.title("🌍 CitySense AI")

    st.subheader("AI-Powered Decision Intelligence Platform")

    st.markdown("---")

    st.write("""
Welcome to **CitySense AI**.

This platform allows you to upload **any CSV or Excel dataset**
and automatically generate:

✅ Interactive Dashboard

✅ Smart Visualizations

✅ AI Insights using Gemini

✅ Forecasting

✅ Anomaly Detection

✅ Decision Intelligence

✅ Data Exploration

No coding required. Just upload your dataset and start analyzing.
""")

    st.info("👈 Use the sidebar to upload your dataset and begin analysis.")
    # ======================================================
# UPLOAD DATASET
# ======================================================

elif page == "📂 Upload Dataset":

    st.title("📂 Upload Dataset")

    st.write(
        "Upload any CSV or Excel dataset for automatic analysis."
    )

    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx", "xls"]
    )

    if uploaded_file is not None:

        try:

            # Read Dataset

            if uploaded_file.name.endswith(".csv"):

                df = pd.read_csv(uploaded_file)

            else:

                df = pd.read_excel(uploaded_file)

            # Clean Dataset

            df = clean_data(df)

            # Save Dataset

            st.session_state.df = df

            st.success("✅ Dataset Uploaded Successfully!")

            st.info(f"Current File: {uploaded_file.name}")

            st.markdown("---")

            # Dataset Metrics

            st.subheader("📊 Dataset Summary")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Rows", df.shape[0])

            col2.metric("Columns", df.shape[1])

            col3.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )

            col4.metric(
                "Duplicate Rows",
                int(df.duplicated().sum())
            )

            st.markdown("---")

            # Preview

            st.subheader("📋 Dataset Preview")

            st.dataframe(
                df.head(20),
                use_container_width=True
            )

            st.markdown("---")

            # Column Information

            st.subheader("📑 Column Information")

            info = pd.DataFrame({

                "Column": df.columns,

                "Data Type": df.dtypes.astype(str),

                "Missing Values": df.isnull().sum().values,

                "Unique Values": df.nunique().values

            })

            st.dataframe(
                info,
                use_container_width=True
            )

            st.markdown("---")

            # Statistical Summary

            st.subheader("📈 Statistical Summary")

            st.dataframe(
                df.describe(include="all").fillna(""),
                use_container_width=True
            )

            st.markdown("---")

            # Download Clean Dataset

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "📥 Download Clean Dataset",
                csv,
                file_name="clean_dataset.csv",
                mime="text/csv"
            )

        except Exception as e:

            st.error(f"❌ Error: {e}")

    else:

        st.info("👆 Upload a CSV or Excel dataset to begin.")
        # ======================================================
# DASHBOARD
# ======================================================

elif page == "📊 Dashboard":

    st.title("📊 Interactive Dashboard")

    df = st.session_state.df

    if df is None:

        st.warning("⚠️ Please upload a dataset first.")

        st.stop()

    st.success("✅ Dataset Loaded Successfully")

    st.markdown("---")

    # ======================================================
    # KPI CARDS
    # ======================================================

    st.subheader("📌 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

    col4.metric(
        "Duplicate Rows",
        int(df.duplicated().sum())
    )

    st.markdown("---")

    # ======================================================
    # COLUMN SELECTION
    # ======================================================

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    categorical_cols = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    # ======================================================
    # DATA PREVIEW
    # ======================================================

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # SHOW PROFESSIONAL DASHBOARD
    # ======================================================

    show_dashboard(df)

    st.markdown("---")

    # ======================================================
    # NUMERIC SUMMARY
    # ======================================================

    if len(numeric_cols) > 0:

        st.subheader("📈 Statistical Summary")

        st.dataframe(
            df[numeric_cols].describe(),
            use_container_width=True
        )

    # ======================================================
    # MISSING VALUES
    # ======================================================

    st.subheader("❗ Missing Values")

    missing = pd.DataFrame({

        "Column": df.columns,

        "Missing Values": df.isnull().sum(),

        "Percentage":

        round(
            (df.isnull().sum()/len(df))*100,
            2
        )

    })

    st.dataframe(
        missing,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================================
    # DOWNLOAD DATASET
    # ======================================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Current Dataset",

        csv,

        file_name="processed_dataset.csv",

        mime="text/csv"

    )
    # ======================================================
# AI ASSISTANT
# ======================================================

elif page == "🤖 AI Assistant":

    st.title("🤖 AI Data Analyst")

    df = st.session_state.df

    if df is None:

        st.warning("⚠️ Please upload a dataset first.")

        st.stop()

    st.write(
        "Ask questions about your uploaded dataset using Gemini AI."
    )

    st.markdown("---")

    # Suggested Questions

    st.subheader("💡 Suggested Questions")

    st.info("""
• Summarize this dataset

• Which column has the highest average?

• Detect unusual patterns.

• Which category occurs most frequently?

• What business insights can you provide?

• Recommend actions based on this dataset.

• Predict possible future trends.

• Explain the important columns.

• Which features are most important?

• Give executive level insights.
""")

    st.markdown("---")

    question = st.text_area(

        "Ask your question",

        height=120,

        placeholder="Example: Which city has the highest average AQI?"

    )

    if st.button("🚀 Generate AI Insight"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Gemini is analyzing your dataset..."):

                try:

                    answer = ask_gemini(question, df)

                    st.success("Analysis Complete")

                    st.markdown(answer)

                except Exception as e:

                    st.error(f"Error: {e}")

    st.markdown("---")

    st.subheader("📄 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Rows", df.shape[0])

        st.metric("Columns", df.shape[1])

    with col2:

        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )
        # ======================================================
# FORECAST
# ======================================================

elif page == "📈 Forecast":

    st.title("📈 Data Forecasting")

    df = st.session_state.df

    if df is None:

        st.warning("⚠️ Please upload a dataset first.")

        st.stop()

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) == 0:

        st.warning("No numeric columns available for forecasting.")

        st.stop()

    st.subheader("Select Column for Forecasting")

    target = st.selectbox(
        "Numeric Column",
        numeric_cols,
        key="forecast_column"
    )

    st.markdown("---")

    forecast_days = st.slider(
        "Forecast Future Points",
        min_value=5,
        max_value=50,
        value=15
    )

    try:

        future = forecast_aqi(
            df,
            target,
            forecast_days
        )

        st.success("Forecast Generated Successfully")

        st.dataframe(
            future,
            use_container_width=True
        )

        st.line_chart(
            future.set_index("Day")
        )

        csv = future.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Forecast",
            csv,
            file_name="forecast.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error(e)
        # ======================================================
# ANOMALY DETECTION
# ======================================================

elif page == "🚨 Anomaly Detection":

    st.title("🚨 Anomaly Detection")

    df = st.session_state.df

    if df is None:

        st.warning("Please upload a dataset first.")

        st.stop()

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) == 0:

        st.warning("No numeric columns found.")

        st.stop()

    column = st.selectbox(
        "Select Numeric Column",
        numeric_cols,
        key="anomaly_column"
    )

    anomalies = detect_anomalies(df, column)

    st.markdown("---")

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Records",
        len(df)
    )

    col2.metric(
        "Anomalies Found",
        len(anomalies)
    )

    st.markdown("---")

    if anomalies.empty:

        st.success("✅ No anomalies detected.")

    else:

        st.error(f"🚨 {len(anomalies)} anomalies detected.")

        st.dataframe(
            anomalies,
            use_container_width=True
        )

        csv = anomalies.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Anomalies",
            csv,
            "anomalies.csv",
            "text/csv"
        )
        # ======================================================
# DECISION INTELLIGENCE
# ======================================================

elif page == "🧠 Decision Intelligence":

    st.title("🧠 AI Decision Intelligence")

    df = st.session_state.df

    if df is None:

        st.warning("Please upload a dataset first.")

        st.stop()

    report = generate_decision_report(df)

    st.success("Decision Report Generated Successfully")
    

    st.markdown("---")

    # Dataset Summary

    st.subheader("📊 Dataset Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        report["Rows"]
    )

    col2.metric(
        "Columns",
        report["Columns"]
    )

    col3.metric(
        "Missing Values",
        report["Missing"]
    )

    st.markdown("---")

    # Numeric Columns

    st.subheader("📈 Numeric Column Analysis")

    st.dataframe(
        report["Statistics"],
        use_container_width=True
    )

    st.markdown("---")

    # Recommendations

    st.subheader("💡 AI Recommendations")

    for rec in report["Recommendations"]:

        st.success(rec)

    st.markdown("---")

    # Download Report

    csv = report["Statistics"].to_csv().encode("utf-8")

    st.download_button(

        "📥 Download Decision Report",

        csv,

        file_name="decision_report.csv",

        mime="text/csv"

    )
    # ======================================================
# ABOUT
# ======================================================

elif page == "ℹ️ About":

    st.title("🌍 About CitySense AI")

    st.markdown("""
# 🌍 CitySense AI

### AI-Powered Decision Intelligence Platform

CitySense AI is a smart analytics platform that enables users to upload any CSV or Excel dataset and instantly generate interactive dashboards, AI-powered insights, forecasting, anomaly detection, and decision intelligence.

---

## 🚀 Features

✅ Upload any CSV or Excel dataset

✅ Automatic Data Cleaning

✅ Interactive Dashboard

✅ Automatic Charts

✅ AI Assistant (Google Gemini)

✅ Forecasting

✅ Anomaly Detection

✅ Decision Intelligence

✅ Download Reports

---

## 📊 Visualizations

- Histogram
- Line Chart
- Scatter Plot
- Bar Chart
- Pie Chart
- Correlation Heatmap

---

## 🤖 Artificial Intelligence

Google Gemini 2.5 Flash analyzes the uploaded dataset and answers natural language questions.

Example Questions:

- Summarize my dataset.
- Which category performs best?
- Detect unusual patterns.
- Recommend business actions.
- Explain important trends.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Google Gemini
- NumPy
- Machine Learning

---

## 👨‍💻 Developed For

Google Cloud Gen AI Academy Hackathon

CitySense AI demonstrates how AI can simplify analytics and help organizations make data-driven decisions.
""")

# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

st.caption(
    "🌍 CitySense AI | AI-Powered Decision Intelligence Platform | Built with ❤️ using Streamlit, Python & Google Gemini"
)