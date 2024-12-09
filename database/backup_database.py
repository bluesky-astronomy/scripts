"""Script to download a backup copy of the entire database."""

from astrofeed_lib.database import db, Post, SubscriptionState, Account, BotActions, ModActions
from pathlib import Path
import pandas as pd


outdir = Path("../data/database_backup")

# Sadly there's no easy way to do this with peewee...
def download_all_posts(table):
    print(f"Downloading all posts for table {table.__name__}...")
    sql, params = table.select().sql()
    dataframe = pd.read_sql_query(sql, db.connection(), params=params)
    print("-> Saving!")
    if table.__name__ == "BotActions":
        dataframe['checked_at'] = dataframe['checked_at'].astype(str)
    dataframe.to_parquet(outdir / f"{table.__name__}.parquet")


for table in (Post, SubscriptionState, Account, BotActions, ModActions):
    download_all_posts(table)