from sqlalchemy import (
    Table, Column, Integer, String, Numeric, Boolean, DateTime, MetaData, ForeignKey
)

metadata = MetaData()

dim_coins = Table(
    "dim_coins",
    metadata,
    Column("coin_id", Integer, primary_key=True),
    Column("symbol", String(100), nullable=False), #BTC, ETH, ADA
    Column("name", String(100), nullable=False), #Bitcoin, Ethereum..
    Column("coingecko_id", String(50), nullable=False), #id usado para o API
)

dim_date = Table(
    "dim_date",
    metadata,
    Column("date_id", Integer, primary_key=True),
    Column("captured_at", DateTime, nullable=False), #timeStampo Completo
    Column("hour", Integer, nullable=False),
    Column("day", Integer, nullable=False),
    Column("month", Integer, nullable=False),
    Column("year", Integer, nullable=False),
    Column("dayofweek", String(50), nullable=False),
    Column("weekend", Boolean, nullable=False),
)

fact_prices = Table("fact_prices", metadata,
                    Column("price_id", Integer, primary_key=True),
                    Column("date_id", Integer, ForeignKey("dim_date.date_id"), nullable=False),
                    Column("coin_id", Integer, ForeignKey("dim_coins.coin_id"), nullable=False),
                    Column("price_usd", Numeric(18,8), nullable=False),
                    Column("market_cap", Numeric(20,2), nullable=False),
                    Column("volume_24h", Numeric(20,2), nullable=False),
                    Column("price_change_pct", Numeric(10,4), nullable=False),) #Coluna derivada