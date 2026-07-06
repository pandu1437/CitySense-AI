import pandas as pd
import numpy as np


def forecast_aqi(df, column, days):

    values = df[column].dropna()

    avg = values.mean()

    trend = np.linspace(
        avg,
        avg * 1.05,
        days
    )

    future = pd.DataFrame({

        "Day": range(1, days + 1),

        column: trend.round(2)

    })

    return future