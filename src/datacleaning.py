"""
data_cleaning.py
----------------
Purpose: 
This script loads a messy sales dataset, applies basic cleaning steps 
(standardizing column names, trimming whitespace, handling missing values, 
and removing invalid rows), and saves the cleaned version to data/processed.
"""

import pandas as pd

# ---------------------------------------------------------------
# Function: load_data
# What it should do: Load a CSV file and return a pandas DataFrame.
# Why: Keeps file loading separate and testable.
# (This is one you should generate using GitHub Copilot)
# ---------------------------------------------------------------
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


# ---------------------------------------------------------------
# Function: clean_column_names
# What it should do: Standardize column names by making them lowercase 
# and replacing spaces with underscores.
# Why: Consistent column names make the data easier to work with.
# ---------------------------------------------------------------
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df


# ---------------------------------------------------------------
# Function: handle_missing_values
# What it should do: Fill or drop missing values in price/quantity.
# Why: Missing values break calculations and indicate incomplete data.
# ---------------------------------------------------------------
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # Example strategy: Drop rows missing price OR quantity
    df = df.dropna(subset=["price", "quantity"])
    return df


# ---------------------------------------------------------------
# Function: remove_invalid_rows
# What it should do: Remove negative quantities and negative prices.
# Why: Negative values are data entry mistakes and should not be included.
# ---------------------------------------------------------------
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["price"] >= 0]
    df = df[df["quantity"] >= 0]
    return df


# ---------------------------------------------------------------
# Run the cleaning pipeline
# ---------------------------------------------------------------
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
    