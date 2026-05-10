from datetime import datetime

COINS = {
        "bitcoin": {"symbol": "BTC", "name": "Bitcoin"},
        "ethereum": {"symbol": "ETH", "name": "Ethereum"},
        "cardano": {"symbol": "ADA", "name": "Cardano"},
    }

def transform_date(now):
    date = {
        "captured_at": now,
        "hour": now.hour,
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "dayofweek": now.strftime("%A"),
        "weekend": now.weekday() >= 5
    }
    return date

def transform_coins(raw_data):
    coins = []
    for item in raw_data:
        coin_id = item["coin_id"]
        coins.append({
            "coingecko_id": coin_id,
            "symbol": COINS[coin_id]["symbol"],
            "name": COINS[coin_id]["name"],
        })
    return coins

def transform_prices(raw_data):
    prices = []
    for item in raw_data:
        coin_id = item["coin_id"]
        prices.append({
            "coin_id": coin_id,
            "price_usd": item["price_usd"],
            "market_cap": item["market_cap"],
            "volume_24h": item["volume_24h"],
            "price_change_pct": item["price_change_pct"],
        })
    return prices

def transform(raw_data):
    now = datetime.now()
    return {
        "date": transform_date(now),
        "coins": transform_coins(raw_data),
        "prices": transform_prices(raw_data),
    }
