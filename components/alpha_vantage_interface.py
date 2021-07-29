import sys

import enquiries

from . import cli_selector
from .alpha_vantage_client import AlphaVantageClient


class AlphaVantageInterface:

    def __init__(self, api_key: str):
        """
        Class to interact with alpha vantage from the cli.

        Args:
            api_key (str): API key for alpha vantage.
        """

        self.client = AlphaVantageClient(api_key)

    def run_cli(self):
        """
        Runs interaction with the user with a cli.
        """

        while True:

            # search for company
            company_name = enquiries.freetext("Search company: ")
            search_options = self.client.search_company(company_name)

            # deal with any error
            if 'Error Message' in search_options:
                selected = enquiries.choose(f"Error Message: {search_options['Error Message']}", ['Search again...'])
                continue
        
            # get the matches
            best_matches = search_options.get('bestMatches')

            # if no matches
            if not best_matches:
                enquiries.choose("None Found!", ['Search again...'])
                continue
            
            # if results were found
            selected_index = cli_selector.select_match(best_matches)

            if selected_index == -1:
                # search again
                continue

    

