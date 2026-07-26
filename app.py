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
# HOME
# ======================================================

# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

/* Main background */

.main {
    background-color:#F8FAFC;
}


/* Sidebar */

section[data-testid="stSidebar"] {

    background:linear-gradient(
        180deg,
        #0f172a,
        #1e3a8a
    );

}


/* Sidebar text */

section[data-testid="stSidebar"] * {

    color:white !important;

}


/* Headings */

h1 {
    color:#1E3A8A;
}

h2 {
    color:#2563EB;
}



/* Metric Cards */

div[data-testid="metric-container"] {

    background:white;

    border-radius:15px;

    padding:18px;

    box-shadow:
    0 8px 20px rgba(0,0,0,0.08);

}


/* Buttons */

.stButton>button {

    background:#2563EB;

    color:white;

    border-radius:10px;

    width:100%;

    font-weight:600;

}


/* ================================
   HERO
================================ */

.hero {

    padding:60px 40px;

    border-radius:30px;

    background:linear-gradient(
        135deg,
        #0f172a,
        #1d4ed8,
        #2563eb
    );

    text-align:center;

    box-shadow:0 15px 40px rgba(0,0,0,0.25);

    margin-bottom:35px;

}


.hero h1 {

    font-size:60px !important;

    font-weight:900 !important;

    color:white !important;

    margin-bottom:20px;

}


.hero h3 {

    font-size:28px !important;

    font-weight:600;

    color:#dbeafe !important;

}


.hero p {

    font-size:18px !important;

    line-height:1.7;

    color:white !important;

}


/* ================================
FEATURE CARDS
================================ */


.feature-card {

    background:white;

    padding:25px;

    border-radius:20px;

    height:190px;

    text-align:center;

    border:1px solid #e2e8f0;

    box-shadow:
    0 8px 25px rgba(0,0,0,0.08);

}


.feature-card h3 {

    color:#2563EB !important;

}


.feature-card p {

    color:#475569 !important;

}



/* ================================
STEP CARDS
================================ */


.step-card {

    background:white;

    padding:20px;

    border-radius:15px;

    border-left:5px solid #2563EB;

}


.step-card h3 {

    color:#1E3A8A !important;

}


.step-card p {

    color:#475569 !important;

}


</style>

""", unsafe_allow_html=True)



# ======================================================
# SESSION STATE
# ======================================================

if "df" not in st.session_state:

    st.session_state.df = None



# ======================================================
# SIDEBAR NAVIGATION
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


# ======================================================
# HOME
# ======================================================

if page == "🏠 Home":


    # ================================
    # HERO SECTION
    # ================================

    st.markdown(
    """
    <div class="hero">

    <h1>🌍 CitySense AI</h1>

    <h3>
    Transform Raw Data Into Intelligent Decisions
    </h3>

    <p>
    An AI-powered decision intelligence platform that converts
    raw datasets into actionable insights using automated analytics,
    predictive AI, and Google Gemini intelligence.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


    # ================================
    # METRICS
    # ================================

    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "📊 Analytics",
            "Automated"
        )


    with col2:
        st.metric(
            "🤖 AI Engine",
            "Gemini"
        )


    with col3:
        st.metric(
            "📁 Data Support",
            "CSV + Excel"
        )


    with col4:
        st.metric(
            "⚡ Processing",
            "Instant"
        )


    st.markdown("---")


    # ================================
    # FEATURES
    # ================================

    st.markdown(
        "## 🚀 Powerful AI Capabilities"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
        """
        <div class="feature-card">

        <h3>📊 Smart Analytics</h3>

        <p>
        Automatically clean, analyze and visualize
        datasets with interactive dashboards.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col2:

        st.markdown(
        """
        <div class="feature-card">

        <h3>🤖 AI Intelligence</h3>

        <p>
        Generate insights and recommendations
        using Google Gemini AI.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col3:

        st.markdown(
        """
        <div class="feature-card">

        <h3>🔮 Predictive AI</h3>

        <p>
        Forecast future trends and detect
        unusual patterns automatically.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    st.markdown("---")


    # ================================
    # HOW IT WORKS
    # ================================

    st.markdown(
        "## ✨ How CitySense AI Works"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
        """
        <div class="step-card">

        <h3>1️⃣ Upload Dataset</h3>

        <p>
        Import CSV or Excel files instantly.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col2:

        st.markdown(
        """
        <div class="step-card">

        <h3>2️⃣ AI Analysis</h3>

        <p>
        AI cleans, explores and discovers
        hidden patterns.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    with col3:

        st.markdown(
        """
        <div class="step-card">

        <h3>3️⃣ Intelligent Decisions</h3>

        <p>
        Generate dashboards, forecasts
        and recommendations.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )


    st.markdown("---")


    st.success(
        "🚀 Ready to unlock intelligence from your data? "
        "Use the sidebar to upload your dataset and start analysis."
    )
    # ======================================================
# UPLOAD DATASET
# ======================================================

# ======================================================
# UPLOAD DATASET
# ======================================================

elif page == "📂 Upload Dataset":

    st.title("📂 Upload Dataset")

    st.markdown(
    """
    Upload your CSV or Excel dataset and let CitySense AI
    automatically clean, analyze and prepare your data.
    """
    )


    st.markdown("---")


    uploaded_file = st.file_uploader(
        "📁 Choose CSV or Excel file",
        type=["csv","xlsx","xls"]
    )


    if uploaded_file is not None:

        try:

            # Read File

            if uploaded_file.name.endswith(".csv"):

                df = pd.read_csv(uploaded_file)

            else:

                df = pd.read_excel(uploaded_file)


            # Cleaning

            with st.spinner("🤖 AI is cleaning your dataset..."):

                df = clean_data(df)


            st.session_state.df = df


            st.success(
                "✅ Dataset uploaded and cleaned successfully!"
            )


            st.info(
                f"📄 File Name : {uploaded_file.name}"
            )


            st.markdown("---")


            # ================================
            # DATASET METRICS
            # ================================

            st.subheader("📊 Dataset Overview")


            col1,col2,col3,col4 = st.columns(4)


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


            # ================================
            # PREVIEW
            # ================================

            st.subheader("📋 Dataset Preview")


            st.dataframe(
                df.head(20),
                use_container_width=True
            )


            st.markdown("---")


            # ================================
            # COLUMN DETAILS
            # ================================

            st.subheader("📑 Column Information")


            column_info = pd.DataFrame({

                "Column Name": df.columns,

                "Data Type": df.dtypes.astype(str),

                "Missing Values":
                df.isnull().sum().values,

                "Unique Values":
                df.nunique().values

            })


            st.dataframe(
                column_info,
                use_container_width=True
            )


            st.markdown("---")


            # ================================
            # STATISTICS
            # ================================

            st.subheader("📈 Statistical Summary")


            st.dataframe(
                df.describe(include="all").fillna(""),
                use_container_width=True
            )


            st.markdown("---")


            # ================================
            # DOWNLOAD
            # ================================

            csv = df.to_csv(
                index=False
            ).encode("utf-8")


            st.download_button(

                "📥 Download Clean Dataset",

                csv,

                file_name="CitySense_clean_dataset.csv",

                mime="text/csv"

            )


        except Exception as e:

            st.error(
                f"❌ Error processing dataset: {e}"
            )


    else:

        st.info(
            "👆 Upload a CSV or Excel file to start AI-powered analysis."
        )
        # ======================================================
# DASHBOARD
# ======================================================

# ======================================================
# DASHBOARD
# ======================================================

elif page == "📊 Dashboard":

    st.title("📊 Intelligent Analytics Dashboard")


    df = st.session_state.df


    if df is None:

        st.warning(
            "⚠️ Please upload a dataset first."
        )

        st.stop()



    st.success(
        "✅ Dataset Loaded Successfully"
    )


    st.markdown("---")


    # ======================================================
    # KPI CARDS
    # ======================================================

    st.subheader("📌 Dataset Intelligence")


    col1,col2,col3,col4 = st.columns(4)


    with col1:

        st.metric(
            "📄 Total Records",
            df.shape[0]
        )


    with col2:

        st.metric(
            "📊 Features",
            df.shape[1]
        )


    with col3:

        st.metric(
            "❗ Missing Values",
            int(df.isnull().sum().sum())
        )


    with col4:

        st.metric(
            "🔁 Duplicate Rows",
            int(df.duplicated().sum())
        )



    st.markdown("---")



    # ======================================================
    # DATA PREVIEW
    # ======================================================


    st.subheader(
        "📋 Dataset Preview"
    )


    st.dataframe(
        df.head(10),
        use_container_width=True
    )



    st.markdown("---")



    # ======================================================
    # AUTOMATIC DASHBOARD
    # ======================================================


    st.subheader(
        "📈 AI Generated Visual Analytics"
    )


    try:

        show_dashboard(df)


    except Exception as e:

        st.error(
            f"Dashboard generation error: {e}"
        )



    st.markdown("---")



    # ======================================================
    # NUMERIC INSIGHTS
    # ======================================================


    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()



    if len(numeric_cols) > 0:


        st.subheader(
            "📊 Numerical Analysis"
        )


        selected_column = st.selectbox(
            "Select column for analysis",
            numeric_cols
        )


        col1,col2 = st.columns(2)



        with col1:

            st.metric(
                "Average",
                round(
                    df[selected_column].mean(),
                    2
                )
            )


        with col2:

            st.metric(
                "Maximum",
                round(
                    df[selected_column].max(),
                    2
                )
            )



        st.line_chart(
            df[selected_column]
        )



    st.markdown("---")



    # ======================================================
    # MISSING VALUE ANALYSIS
    # ======================================================


    st.subheader(
        "🔍 Data Quality Report"
    )


    quality = pd.DataFrame({

        "Column":
        df.columns,

        "Missing":
        df.isnull().sum(),

        "Unique Values":
        df.nunique(),

        "Data Type":
        df.dtypes.astype(str)

    })


    st.dataframe(
        quality,
        use_container_width=True
    )



    st.markdown("---")



    # ======================================================
    # DOWNLOAD
    # ======================================================


    csv = df.to_csv(
        index=False
    ).encode("utf-8")



    st.download_button(

        "📥 Export Dashboard Dataset",

        csv,

        file_name="CitySense_dashboard_data.csv",

        mime="text/csv"

    )
    # ======================================================
# AI ASSISTANT
# ======================================================

# ======================================================
# AI ASSISTANT
# ======================================================

elif page == "🤖 AI Assistant":

    st.title("🤖 CitySense AI Analyst")


    df = st.session_state.df


    if df is None:

        st.warning(
            "⚠️ Please upload a dataset first."
        )

        st.stop()



    st.markdown(
    """
    Ask questions about your dataset and get
    AI-powered insights, recommendations and explanations
    using Google Gemini.
    """
    )


    st.markdown("---")


    # ======================================================
    # DATASET SUMMARY CARD
    # ======================================================


    st.subheader(
        "📊 Current Dataset"
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(
            "Rows",
            df.shape[0]
        )


    with col2:

        st.metric(
            "Columns",
            df.shape[1]
        )


    with col3:

        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )


    st.markdown("---")



    # ======================================================
    # AI SUGGESTIONS
    # ======================================================


    st.subheader(
        "💡 Try Asking"
    )


    suggestions = [

        "Summarize this dataset",

        "Find important trends",

        "Detect unusual patterns",

        "Give business recommendations",

        "Explain important columns",

        "Predict future trends"

    ]


    cols = st.columns(3)


    for i, suggestion in enumerate(suggestions):

        with cols[i % 3]:

            st.info(
                suggestion
            )



    st.markdown("---")



    # ======================================================
    # USER QUERY
    # ======================================================


    question = st.text_area(

        "💬 Ask your AI Data Analyst",

        placeholder=
        "Example: Which city has the highest AQI level?",

        height=120

    )



    if st.button(
        "🚀 Generate AI Insight"
    ):


        if question.strip() == "":


            st.warning(
                "Please enter a question."
            )


        else:


            with st.spinner(
                "🤖 Gemini is analyzing your dataset..."
            ):


                try:


                    answer = ask_gemini(
                        question,
                        df
                    )


                    st.markdown("---")


                    st.subheader(
                        "🧠 AI Response"
                    )


                    st.success(
                        "Analysis Completed"
                    )


                    st.write(
                        answer
                    )



                except Exception as e:


                    st.error(
                        f"AI Error: {e}"
                    )



    st.markdown("---")



    # ======================================================
    # DATA SAMPLE
    # ======================================================


    st.subheader(
        "📋 Dataset Sample"
    )


    st.dataframe(

        df.head(10),

        use_container_width=True

    )
        # ======================================================
# FORECAST
# ======================================================

# ======================================================
# FORECAST
# ======================================================

elif page == "📈 Forecast":

    st.title("📈 Predictive AI Forecasting")


    df = st.session_state.df


    if df is None:

        st.warning(
            "⚠️ Please upload a dataset first."
        )

        st.stop()



    st.markdown(
    """
    Use machine learning techniques to forecast future
    trends and understand possible upcoming patterns.
    """
    )


    st.markdown("---")



    # ======================================================
    # SELECT COLUMN
    # ======================================================


    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()



    if len(numeric_cols) == 0:

        st.warning(
            "No numerical columns available for forecasting."
        )

        st.stop()



    st.subheader(
        "🎯 Select Forecast Target"
    )


    target = st.selectbox(

        "Choose numerical column",

        numeric_cols

    )



    forecast_points = st.slider(

        "🔮 Future Prediction Points",

        min_value=5,

        max_value=50,

        value=15

    )



    st.markdown("---")



    # ======================================================
    # CURRENT DATA INSIGHTS
    # ======================================================


    st.subheader(
        "📊 Current Data Overview"
    )


    col1,col2,col3 = st.columns(3)



    with col1:

        st.metric(

            "Average",

            round(
                df[target].mean(),
                2
            )

        )



    with col2:

        st.metric(

            "Maximum",

            round(
                df[target].max(),
                2
            )

        )



    with col3:

        st.metric(

            "Minimum",

            round(
                df[target].min(),
                2
            )

        )



    st.markdown("---")



    # ======================================================
    # FORECAST GENERATION
    # ======================================================


    if st.button(
        "🚀 Generate Forecast"
    ):


        with st.spinner(
            "🤖 AI model is predicting future trends..."
        ):


            try:


                future = forecast_aqi(

                    df,

                    target,

                    forecast_points

                )


                st.success(
                    "✅ Forecast Generated Successfully"
                )


                st.markdown("---")



                # Forecast Table


                st.subheader(
                    "📋 Prediction Results"
                )


                st.dataframe(

                    future,

                    use_container_width=True

                )



                st.markdown("---")



                # Chart


                st.subheader(
                    "📈 Forecast Visualization"
                )


                st.line_chart(

                    future.set_index(
                        "Day"
                    )

                )



                st.markdown("---")



                # Download


                csv = future.to_csv(
                    index=False
                ).encode(
                    "utf-8"
                )


                st.download_button(

                    "📥 Download Forecast Report",

                    csv,

                    file_name=
                    "CitySense_forecast_report.csv",

                    mime=
                    "text/csv"

                )



            except Exception as e:


                st.error(
                    f"Forecast Error: {e}"
                )
        # ======================================================
# ANOMALY DETECTION
# ======================================================

# ======================================================
# ANOMALY DETECTION
# ======================================================

elif page == "🚨 Anomaly Detection":

    st.title("🚨 AI Anomaly Detection")


    df = st.session_state.df


    if df is None:

        st.warning(
            "⚠️ Please upload a dataset first."
        )

        st.stop()



    st.markdown(
    """
    Detect unusual patterns, abnormal values and
    potential risks in your dataset using machine learning.
    """
    )


    st.markdown("---")



    # ======================================================
    # COLUMN SELECTION
    # ======================================================


    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()



    if len(numeric_cols) == 0:

        st.warning(
            "No numerical columns available for anomaly detection."
        )

        st.stop()



    st.subheader(
        "🎯 Select Data Feature"
    )


    column = st.selectbox(

        "Choose numerical column",

        numeric_cols

    )



    st.markdown("---")



    # ======================================================
    # DATA SUMMARY
    # ======================================================


    st.subheader(
        "📊 Feature Statistics"
    )


    col1,col2,col3,col4 = st.columns(4)



    with col1:

        st.metric(
            "Total Records",
            len(df)
        )



    with col2:

        st.metric(
            "Average Value",
            round(
                df[column].mean(),
                2
            )
        )



    with col3:

        st.metric(
            "Maximum",
            round(
                df[column].max(),
                2
            )
        )



    with col4:

        st.metric(
            "Minimum",
            round(
                df[column].min(),
                2
            )
        )



    st.markdown("---")



    # ======================================================
    # DETECTION
    # ======================================================


    if st.button(
        "🚀 Detect Anomalies"
    ):


        with st.spinner(
            "🤖 AI model is scanning your data..."
        ):


            try:


                anomalies = detect_anomalies(

                    df,

                    column

                )


                st.success(
                    "✅ Anomaly Detection Completed"
                )


                st.markdown("---")



                # RESULTS


                st.subheader(
                    "🚨 Detection Results"
                )


                col1,col2 = st.columns(2)



                with col1:

                    st.metric(

                        "Total Records",

                        len(df)

                    )



                with col2:

                    st.metric(

                        "Anomalies Found",

                        len(anomalies)

                    )



                st.markdown("---")



                if anomalies.empty:


                    st.success(
                        "🎉 No unusual patterns detected."
                    )



                else:


                    st.error(
                        f"🚨 {len(anomalies)} abnormal records detected"
                    )


                    st.dataframe(

                        anomalies,

                        use_container_width=True

                    )



                    st.markdown("---")



                    st.subheader(
                        "📈 Anomaly Visualization"
                    )


                    st.line_chart(

                        df[column]

                    )



                    st.markdown("---")



                    csv = anomalies.to_csv(
                        index=False
                    ).encode(
                        "utf-8"
                    )



                    st.download_button(

                        "📥 Download Anomaly Report",

                        csv,

                        file_name=
                        "CitySense_anomaly_report.csv",

                        mime=
                        "text/csv"

                    )



            except Exception as e:


                st.error(
                    f"Anomaly Detection Error: {e}"
                )
        # ======================================================
# DECISION INTELLIGENCE
# ======================================================

# ======================================================
# DECISION INTELLIGENCE
# ======================================================

elif page == "🧠 Decision Intelligence":

    st.title("🧠 AI Decision Intelligence")


    df = st.session_state.df


    if df is None:

        st.warning(
            "⚠️ Please upload a dataset first."
        )

        st.stop()



    st.markdown(
    """
    Transform raw analytics into actionable decisions.
    CitySense AI analyzes your data and generates
    recommendations, business insights and strategic actions.
    """
    )


    st.markdown("---")



    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================


    st.subheader(
        "📊 Executive Data Summary"
    )


    col1,col2,col3,col4 = st.columns(4)



    with col1:

        st.metric(
            "Total Records",
            df.shape[0]
        )


    with col2:

        st.metric(
            "Data Features",
            df.shape[1]
        )


    with col3:

        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )


    with col4:

        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )



    st.markdown("---")



    # ======================================================
    # GENERATE REPORT
    # ======================================================


    if st.button(
        "🚀 Generate AI Decision Report"
    ):


        with st.spinner(
            "🤖 AI is generating strategic insights..."
        ):


            try:


                report = generate_decision_report(df)



                st.success(
                    "✅ Decision Report Generated"
                )



                st.markdown("---")



                # ======================================================
                # STATISTICS
                # ======================================================


                st.subheader(
                    "📈 Data Intelligence"
                )


                if "Statistics" in report:


                    st.dataframe(

                        report["Statistics"],

                        use_container_width=True

                    )



                st.markdown("---")



                # ======================================================
                # RECOMMENDATIONS
                # ======================================================


                st.subheader(
                    "💡 AI Recommendations"
                )


                if "Recommendations" in report:


                    for recommendation in report["Recommendations"]:


                        st.success(
                            recommendation
                        )



                st.markdown("---")



                # ======================================================
                # BUSINESS ACTIONS
                # ======================================================


                st.subheader(
                    "🎯 Recommended Actions"
                )


                actions = [

                    "📌 Monitor important performance indicators regularly.",

                    "📌 Investigate unusual patterns detected in data.",

                    "📌 Optimize decisions using predictive insights.",

                    "📌 Use AI-generated trends for future planning."

                ]


                for action in actions:


                    st.info(
                        action
                    )



                st.markdown("---")



                # ======================================================
                # DOWNLOAD REPORT
                # ======================================================


                if "Statistics" in report:


                    csv = report["Statistics"].to_csv().encode(
                        "utf-8"
                    )


                    st.download_button(

                        "📥 Download Decision Report",

                        csv,

                        file_name=
                        "CitySense_AI_Decision_Report.csv",

                        mime=
                        "text/csv"

                    )



            except Exception as e:


                st.error(
                    f"Decision Intelligence Error: {e}"
                )
    # ======================================================
# ABOUT
# ======================================================

# ======================================================
# ABOUT
# ======================================================

elif page == "ℹ️ About":

    st.title("🌍 About CitySense AI")


    st.markdown(
    """
    <div class="hero">

    <h1>
    CitySense AI
    </h1>

    <h3>
    AI-Powered Decision Intelligence Platform
    </h3>

    <p>
    Turning raw data into intelligent decisions using
    Artificial Intelligence, Machine Learning and Google Gemini.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


    st.markdown("---")


    # ======================================================
    # PROJECT OVERVIEW
    # ======================================================


    st.subheader(
        "🚀 Project Overview"
    )


    st.write(
    """
    CitySense AI is an intelligent analytics platform that enables
    users to upload datasets and instantly generate insights,
    dashboards, predictions and recommendations.

    The platform combines automated data processing,
    machine learning models and Generative AI to simplify
    complex data analysis.
    """
    )


    st.markdown("---")



    # ======================================================
    # FEATURES
    # ======================================================


    st.subheader(
        "✨ Core Capabilities"
    )


    col1,col2,col3 = st.columns(3)



    with col1:

        st.info(
        """
        📊 Smart Analytics

        • Automated data cleaning

        • Interactive dashboards

        • Data exploration

        """
        )



    with col2:

        st.info(
        """
        🤖 Generative AI

        • Gemini AI assistant

        • Natural language analysis

        • Intelligent recommendations

        """
        )



    with col3:

        st.info(
        """
        🔮 Predictive Intelligence

        • Forecasting

        • Trend analysis

        • Anomaly detection

        """
        )



    st.markdown("---")



    # ======================================================
    # TECHNOLOGY STACK
    # ======================================================


    st.subheader(
        "🛠 Technology Stack"
    )


    tech = pd.DataFrame({

        "Category":[

            "Programming",

            "Analytics",

            "Visualization",

            "AI",

            "Framework"

        ],

        "Technology":[

            "Python",

            "Pandas, NumPy, Scikit-learn",

            "Plotly, Streamlit Charts",

            "Google Gemini AI",

            "Streamlit"

        ]

    })


    st.dataframe(

        tech,

        use_container_width=True,

        hide_index=True

    )



    st.markdown("---")



    # ======================================================
    # AI ARCHITECTURE
    # ======================================================


    st.subheader(
        "🏗 How CitySense AI Works"
    )


    architecture = [

        "1️⃣ User uploads CSV / Excel dataset",

        "2️⃣ Data cleaning and preprocessing",

        "3️⃣ Automated analytics and visualization",

        "4️⃣ Machine learning forecasting",

        "5️⃣ Gemini AI generates insights",

        "6️⃣ Decision recommendations are created"

    ]


    for step in architecture:

        st.success(step)



    st.markdown("---")



    # ======================================================
    # DEVELOPER SECTION
    # ======================================================


    st.subheader(
        "👨‍💻 Built With"
    )


    st.write(
    """
    ❤️ Built using Python, Streamlit, Machine Learning
    and Google Gemini AI.

    Created for demonstrating how Artificial Intelligence
    can transform traditional analytics into intelligent
    decision-making systems.
    """
    )

# ======================================================
# FOOTER
# ======================================================

st.markdown(
"""
<hr>

<div style="
text-align:center;
padding:20px;
font-size:15px;
color:#64748b;
">

<h3 style="color:#2563EB;">
🌍 CitySense AI
</h3>

<p>
AI-Powered Decision Intelligence Platform
</p>

<p>
Built with ❤️ using Python • Streamlit • Google Gemini • Machine Learning
</p>

<p>
© 2026 CitySense AI | Turning Data Into Intelligence
</p>

</div>

""",
unsafe_allow_html=True
)
