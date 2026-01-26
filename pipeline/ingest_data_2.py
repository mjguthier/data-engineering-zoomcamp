import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")

files_and_tables = [
    ("green_tripdata_2025-11.parquet",  "green_tripdata_2025_11"),
]

for filepath, table in files_and_tables:
    print(f"Reading {filepath} ...")
    df = pd.read_parquet(filepath)

    print(f"Loading into {table} ({len(df):,} rows) ...")
    df.to_sql(table, engine, if_exists="replace", index=False)

print("Done.")
