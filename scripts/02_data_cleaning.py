"""
Project : Mutual Fund Analytics
Author  : Simran
Purpose : Clean all raw datasets and generate a cleaning summary.
"""

from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
REPORT_PATH = Path("reports/logs")

PROCESSED_PATH.mkdir(exist_ok=True)
REPORT_PATH.mkdir(parents=True, exist_ok=True)

summary = []

print("=" * 80)
print("MUTUAL FUND ANALYTICS")
print("Universal Data Cleaning Pipeline")
print("=" * 80)

csv_files = sorted(RAW_PATH.glob("*.csv"))

for file in csv_files:

    print(f"\nProcessing : {file.name}")

    df = pd.read_csv(file)

    original_rows = len(df)

    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    # Clean text columns
    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    invalid_dates = 0

    # Automatically convert date columns
    for col in df.columns:

        if "date" in col.lower() or "month" in col.lower():

            converted = pd.to_datetime(df[col], errors="coerce")

            invalid_dates += converted.isna().sum()

            df[col] = converted

    output_file = PROCESSED_PATH / f"{file.stem}_clean.csv"

    df.to_csv(output_file, index=False)

    summary.append({
        "Dataset": file.name,
        "Original Rows": original_rows,
        "Final Rows": len(df),
        "Duplicates Removed": duplicates,
        "Invalid Dates": invalid_dates
    })

summary_df = pd.DataFrame(summary)

summary_df.to_csv(
    REPORT_PATH / "cleaning_summary.csv",
    index=False
)

print("\nCleaning completed successfully.")

print(summary_df)