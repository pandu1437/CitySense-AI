import pandas as pd


def detect_anomalies(df, column):

    data = df.copy()

    data = data.dropna(subset=[column])

    Q1 = data[column].quantile(0.25)

    Q3 = data[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR

    upper = Q3 + 1.5 * IQR

    anomalies = data[
        (data[column] < lower) |
        (data[column] > upper)
    ].copy()

    anomalies["Anomaly"] = "Yes"

    return anomalies