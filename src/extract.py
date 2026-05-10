import logging
import requests
from requests import exceptions

def get(url, prms):
    try:
        resp = requests.get(url, params= prms , timeout=10)
        resp.raise_for_status()
        return resp.json()
    except exceptions.HTTPError as err:
        logging.error(f"HTTP Error: {err}")
    except exceptions.ConnectionError as err:
        logging.error(f"Connection Error: {err}")
    except exceptions.Timeout as err:
        logging.error(f"Timeout Error: {err}")
    return None

def extract():

    url= "https://api.coingecko.com/api/v3/simple/price"
    prms = {
        "ids" : "bitcoin,ethereum,cardano",
        "vs_currencies" : "usd",
        "include_market_cap" : "true",
        "include_24hr_vol" : "true",
        "include_24hr_change" : "true",
    }

    data = get(url, prms)

    if data is None:
        return None

    raw_data = []
    for coin_id, values in data.items():
        raw_data.append({
            "coin_id": coin_id,
            "price_usd": values["usd"],
            "market_cap": values["usd_market_cap"],
            "volume_24hr": values["usd_24h_vol"],
            "price_change_pct": values["usd_24h_change"],
        })
    return raw_data