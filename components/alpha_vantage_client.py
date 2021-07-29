import requests
import sys

from urllib.parse import urlencode
from typing import Dict, Any


class AlphaVantageClient:

    def __init__(self, api_key: str):
        """
        Client to query Alpha Vantage.

        Args:
            api_key (str): API Key for Alpha Vantage to be used in querying.
        """
        self.base_url = "https://www.alphavantage.co/"
        self.api_key = api_key

    def search_company(self, company_name: str) -> Dict[Any, Any]:
        """
        Searches for 'company_name' using SYMBOL_SEARCH and returns the result.

        Args:
            company_name (str): The company name to search for.

        Returns:
            Dict[Any, Any]: The data returned from the search.
        """
        return self._query(function="SYMBOL_SEARCH", keywords=company_name)
    
    def get_weekly_prices(self, symbol: str) -> Dict[Any, Any]:
        """
        Gets weekly prices for a symbol.

        Args:
            symbol (str): Symbol to get prices for.

        Returns:
            Dict[Any, Any]: The data returned from the url.
        """
        return self._query(function="TIME_SERIES_WEEKLY", symbol=symbol)
    
    def get_daily_prices(self, symbol: str) -> Dict[Any, Any]:
        """
        Gets daily prices for a symbol.

        Args:
            symbol (str): Symbol to get prices for.

        Returns:
            Dict[Any, Any]: The data returned from the url.
        """
        return self._query(function="TIME_SERIES_DAILY", symbol=symbol)
    
    def get_current_quote(self, symbol: str) -> Dict[Any, Any]:
        """
        Gets current quote a symbol.

        Args:
            symbol (str): Symbol to get quote for.

        Returns:
            Dict[Any, Any]: The data returned from the url.
        """
        return self._query(function="GLOBAL_QUOTE", symbol=symbol)
    
    def get_indicators(self, symbol: str) -> Dict[Any, Any]:
        """
        Gets indicators for a symbol.

        Args:
            symbol (str): Symbol to get indicators for.

        Returns:
            Dict[Any, Any]: The data returned from the url.
        """
        return self._query(function="SMA", symbol=symbol, interval="weekly", time_period=10, series_type="open")

    def _query(self, **kwargs: str) -> Dict[Any, Any]:
        """
        Queries alpha vantage with given kwargs.

        Args:
            **kwargs (str): kwargs to add to the query. 

        Returns:
            Dict[Any, Any]: The data returned by the query.
        """
        url = self._generate_query_url(self.base_url, self.api_key, **kwargs)
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as err:
            print(f"Unable to retrieve data from {url}")
            print(f"Error: {err}")
            sys.exit(0)
        return data
    
    @staticmethod
    def _generate_query_url(base_url: str, api_key: str, **kwargs: str) -> str:
        """
        Generates a query url given a base url, api key and query kwargs.

        Args:
            base_url (str): The base url. E.g. www.example.com
            api_key (str): The api key. E.g. abc.
            **kwargs (str): Query keyword args. E.g. function=test.

        Returns:
            str: The query url... {base_url}/query?{*}&apikey={api_key}. 
                E.g. www.example.com/query?function=test&api_key=abc for above example args.
        """
        query_args = urlencode(list(kwargs.items()))
        query_url = f"{base_url.rstrip('/')}/query?{query_args}&apikey={api_key}"
        return query_url
