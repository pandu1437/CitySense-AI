import streamlit as st
import plotly.express as px
import pandas as pd


def show_dashboard(df):

    # ----------------------------
    # Numeric & Categorical Columns
    # ----------------------------

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    # ----------------------------
    # Dataset Preview
    # ----------------------------

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---")

    # ----------------------------
    # Histogram
    # ----------------------------

    if len(numeric_cols) > 0:

        st.subheader("📊 Histogram")

        column = st.selectbox(
            "Select Numeric Column",
            numeric_cols,
            key="dashboard_histogram"
        )

        fig = px.histogram(
            df,
            x=column,
            title=f"Distribution of {column}"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Line Chart
    # ----------------------------

    if len(numeric_cols) > 0:

        st.subheader("📈 Line Chart")

        column = st.selectbox(
            "Select Line Chart Column",
            numeric_cols,
            key="dashboard_line"
        )

        fig = px.line(
            df,
            y=column,
            title=f"{column} Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Bar Chart
    # ----------------------------

    if len(categorical_cols) > 0:

        st.subheader("📊 Category Counts")

        cat = st.selectbox(
            "Select Category",
            categorical_cols,
            key="dashboard_bar"
        )

        counts = df[cat].value_counts().reset_index()

        counts.columns = [cat, "Count"]

        fig = px.bar(
            counts,
            x=cat,
            y="Count",
            color="Count",
            title=f"{cat} Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Pie Chart
    # ----------------------------

    if len(categorical_cols) > 0:

        st.subheader("🥧 Pie Chart")

        cat = st.selectbox(
            "Select Pie Column",
            categorical_cols,
            key="dashboard_pie"
        )

        counts = df[cat].value_counts().reset_index()

        counts.columns = [cat, "Count"]

        fig = px.pie(
            counts,
            names=cat,
            values="Count",
            title=f"{cat} Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Scatter Plot
    # ----------------------------

    if len(numeric_cols) >= 2:

        st.subheader("🎯 Scatter Plot")

        x = st.selectbox(
            "X Axis",
            numeric_cols,
            key="dashboard_scatter_x"
        )

        y = st.selectbox(
            "Y Axis",
            numeric_cols,
            key="dashboard_scatter_y"
        )

        fig = px.scatter(
            df,
            x=x,
            y=y,
            title=f"{x} vs {y}"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Correlation Heatmap
    # ----------------------------

    if len(numeric_cols) >= 2:

        st.subheader("🔥 Correlation Matrix")

        corr = df[numeric_cols].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Correlation Heatmap"
        )

        st.plotly_chart(fig, use_container_width=True)