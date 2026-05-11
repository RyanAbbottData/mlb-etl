# For SQL Server with username/password
import os
import uuid

import pandas as pd
import sqlalchemy
from dotenv import load_dotenv


load_dotenv()

# Fetch variables
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

def write_to_sql(data,
                 table):
    
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

    engine = sqlalchemy.create_engine(DATABASE_URL)

    # if isinstance(data, list[dict]):
    df = pd.DataFrame(data)

    if isinstance(data, pd.DataFrame):
        df = data

    with engine.begin() as conn:
        result = df.to_sql(table, con=conn, if_exists='append', index=False)
        print(f"to_sql returned: {result}")

def read_sql(query):
    
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

    engine = sqlalchemy.create_engine(DATABASE_URL)

    df = pd.read_sql(query, con=engine)

    return df