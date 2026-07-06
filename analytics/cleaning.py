import pandas as pd

def clean_data(df):

    df = df.copy()

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert Date column only if it exists
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )

    # Fill missing numeric values
    numeric_cols = df.select_dtypes(include="number").columns

    df[numeric_cols] = df[numeric_cols].fillna(
        df[numeric_cols].median()
    )

    return df