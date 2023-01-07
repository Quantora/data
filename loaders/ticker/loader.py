import os
import polygon
import core

from typing import Any
from polygon.rest.models.tickers import Ticker, TickerDetails


POLYGON_API_KEY = os.getenv('POLYGON_API_KEY', '')
polygon_client = polygon.RESTClient(POLYGON_API_KEY)


def load_all(market: str, type: str) -> list[str]:
    tickers: list[str] = []

    for ticker in polygon_client.list_tickers(market=market, type=type, limit=1000):
        ticker = core.ensure_type(ticker, Ticker)

        if ticker.ticker:
            tickers.append(ticker.ticker)

    return tickers


def load_details(ticker: str) -> dict[str, Any]:
    data = polygon_client.get_ticker_details(ticker)
    data = core.ensure_type(data, TickerDetails)

    return dict(
        ticker=data.ticker,
        name=data.name,
        listed_date=data.list_date,
        sic_code=data.sic_code,
        market_cap=data.market_cap,
        weighted_shares=data.weighted_shares_outstanding
    )
