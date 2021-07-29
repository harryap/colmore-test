import requests

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
    
    def _query(self, **kwargs: str) -> Dict[Any, Any]:
        """

        Args:
            **kwargs (str): kwargs to add to the query. 

        Returns:
            Dict[Any, Any]: The data returned by the query.
        """
        url = self._generate_query_url(self.base_url, self.api_key, **kwargs)
        response = requests.get(url)
        data = response.json()
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
