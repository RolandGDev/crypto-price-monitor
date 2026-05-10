from sqlalchemy import insert
from models import dim_date, dim_coins, fact_prices


def load_dim_dates(conn, date):
   conn.execute(insert(dim_date),date)

def load_coins(conn, coins):
    conn.execute(insert(dim_coins),coins)

def load_fact_prices(conn, facts):
    conn.execute(insert(fact_prices),facts)

def load (engine, transformed_data):
    with engine.connect() as conn:
        load_dim_dates(conn, transformed_data["date"])
        load_coins(conn, transformed_data["coins"])
        load_fact_prices(conn, transformed_data["prices"])
        conn.commit()