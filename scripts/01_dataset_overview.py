from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw")

print("=" * 80)
print("MUTUAL FUND ANALYTICS")
print("Dataset Profiling Report")
print("=" * 80)

csv_files = sorted(RAW_DATA_PATH.glob("*.csv"))

for file in csv_files:
    df = pd.read_csv(file)

    print("\n" + "=" * 80)
    print(f"Dataset : {file.name}")
    print("=" * 80)

    print(f"Rows            : {df.shape[0]}")
    print(f"Columns         : {df.shape[1]}")

    memory = df.memory_usage(deep=True).sum() / 1024
    print(f"Memory Usage    : {memory:.2f} KB")

    print(f"Duplicate Rows  : {df.duplicated().sum()}")

    print("\nColumn Summary")
    print("-" * 80)

    summary = pd.DataFrame({
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum(),
        "Missing %": ((df.isnull().sum() / len(df)) * 100).round(2)
    })

    print(summary)

print("\n")
print("=" * 80)
print("Dataset profiling completed successfully.")
print("=" * 80)