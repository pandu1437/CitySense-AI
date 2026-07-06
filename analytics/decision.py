import pandas as pd


def generate_decision_report(df):

    numeric = df.select_dtypes(include="number")

    report = {}

    report["Rows"] = df.shape[0]

    report["Columns"] = df.shape[1]

    report["Missing"] = int(df.isnull().sum().sum())

    if len(numeric.columns) > 0:

        report["Statistics"] = numeric.describe().T

    else:

        report["Statistics"] = pd.DataFrame()

    recommendations = []

    if report["Missing"] > 0:

        recommendations.append(
            "Dataset contains missing values. Consider cleaning them."
        )

    else:

        recommendations.append(
            "No missing values detected."
        )

    if df.duplicated().sum() > 0:

        recommendations.append(
            "Duplicate rows found. Consider removing duplicates."
        )

    else:

        recommendations.append(
            "No duplicate rows found."
        )

    if len(numeric.columns) > 0:

        recommendations.append(
            "Numeric columns are available for forecasting and anomaly detection."
        )

    else:

        recommendations.append(
            "No numeric columns available."
        )

    report["Recommendations"] = recommendations

    return report