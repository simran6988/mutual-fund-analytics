from pathlib import Path
import pandas as pd

# Mutual Fund Analytics
# Data Cleaning Pipeline

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

# Create processed folder if it doesn't exist
PROCESSED_PATH.mkdir(exist_ok=True)

print("=" * 80)
print("MUTUAL FUND ANALYTICS")
print("Data Cleaning Pipeline")
print("=" * 80)

# Load dataset
df = pd.read_csv(RAW_PATH / "01_fund_master.csv")

print(f"\nOriginal Shape : {df.shape}")

# Remove duplicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

# Remove leading/trailing spaces from text columns
text_columns = df.select_dtypes(include="object").columns
for column in text_columns:
    df[column] = df[column].str.strip()

# Convert launch_date into datetime
df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)
print(f"Invalid Dates    : {df['launch_date'].isna().sum()}")
print(f"Duplicates Removed : {duplicates}")
print(f"Final Shape        : {df.shape}")

# Save cleaned dataset
output_file = PROCESSED_PATH / "01_fund_master_clean.csv"
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully.")
print(output_file)