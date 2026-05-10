from sqlalchemy import insert, select
from models import dim_date, dim_coins, fact_prices


def load_dim_dates(conn, date):
   conn.execute(insert(dim_date),date)

def load_coins(conn, coins):
    conn.execute(insert(dim_coins),coins)

def load_fact_prices(conn, facts):
    results = conn.execute(select(dim_coins.c.coin_id, dim_coins.c.coingecko_id))
    date_result = conn.execute(select(dim_date.c.date_id).order_by(dim_date.c.date_id.desc()).limit(1))
    date_id = date_result.scalar()
    coin_map = {}
    for row in results:
        coin_map[row.coingecko_id] = row.coin_id
    for price in facts:
       price["coin_id"] = coin_map[price["coin_id"]]
       price["date_id"] = date_id
    conn.execute(insert(fact_prices), facts)


def load (engine, transformed_data):
    with engine.connect() as conn:
        load_dim_dates(conn, transformed_data["date"])
        load_coins(conn, transformed_data["coins"])
        load_fact_prices(conn, transformed_data["prices"])
        conn.commit()