"""Script to download contents of the posts database."""

from astrofeed_lib.database import db, Post, Account
import pandas as pd


# Grab posts
query = Post.select().where(Post.feed_astro)  # .limit(50)
sql, params = query.sql()

dataframe = pd.read_sql_query(sql, db.connection(), params=params)
dataframe.to_parquet("../data/feed_astro_posts.parquet")


# We also need a list of authors to filter posts by only valid authorsm so we may as
# well get that too
query = Account.select()  # .limit(50)
sql, params = query.sql()

dataframe = pd.read_sql_query(sql, db.connection(), params=params)
dataframe.to_parquet("../data/accounts.parquet")
