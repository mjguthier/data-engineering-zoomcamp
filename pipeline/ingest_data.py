#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

TRIPS_DTYPE = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

TRIPS_PARSE_DATES = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

ZONES_URL = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

@click.command()
@click.option("--pg-user", default="root", help="PostgreSQL user")
@click.option("--pg-pass", default="root", help="PostgreSQL password")
@click.option("--pg-host", default="localhost", help="PostgreSQL host")
@click.option("--pg-port", default=5432, type=int, help="PostgreSQL port")
@click.option("--pg-db", default="ny_taxi", help="PostgreSQL database name")
@click.option("--dataset", type=click.Choice(["trips", "zones"]), default="trips",
              help="Which dataset to ingest")
@click.option("--year", default=2021, type=int, help="Year of the trips data")
@click.option("--month", default=1, type=int, help="Month of the trips data")
@click.option("--target-table", default=None, help="Target table name (optional)")
@click.option("--chunksize", default=100000, type=int, help="Chunk size for reading trips CSV")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, dataset, year, month, target_table, chunksize):
    engine = create_engine(f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")

    if dataset == "zones":
        table = target_table or "zones"
        df = pd.read_csv(ZONES_URL)

        # Replace table each time (lookup table)
        df.to_sql(name=table, con=engine, if_exists="replace", index=False)
        print(f"Loaded {len(df):,} rows into {table}")
        return

    # dataset == "trips"
    table = target_table or "yellow_taxi_trips"
    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"
    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"

    df_iter = pd.read_csv(
        url,
        dtype=TRIPS_DTYPE,
        parse_dates=TRIPS_PARSE_DATES,
        iterator=True,
        chunksize=chunksize,
    )

    first = True
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(name=table, con=engine, if_exists="replace", index=False)
            first = False
        df_chunk.to_sql(name=table, con=engine, if_exists="append", index=False)

    print(f"Loaded trips into {table} from {url}")

if __name__ == "__main__":
    run()
