import sys

import enquiries
import pandas as pd

from tabulate import tabulate

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

        try:
            self._run_cli()
        except KeyboardInterrupt:
            sys.exit()

    def _run_cli(self):
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

            # get selected company
            selected_company_data = best_matches[selected_index]
            selected_symbol = selected_company_data['1. symbol']

            while True:

                # get desired user action
                action = enquiries.choose(
                    "Options:", 
                    [
                        "Additional Details", "Historic Prices", "Current Quote", 
                        "Indicator Results", "Search Again..."
                    ]
                )

                # init var for printing info to user
                show_strings = []

                # search again
                if action == "Search Again...":
                    break
                
                # additional details
                elif action == "Additional Details":
                    show_strings.append(tabulate([[key, value] for key, value in selected_company_data.items()]))
                
                # historic prices
                elif action == "Historic Prices":

                    # options
                    timeframe = enquiries.choose(
                        "Select Timeframe:", 
                        ["Daily", "Weekly"]
                    )
                    if timeframe == "Daily":
                        data = self.client.get_daily_prices(selected_symbol)
                    elif timeframe == "Weekly":
                        data = self.client.get_weekly_prices(selected_symbol)
                    
                    # build visual for user
                    for key, value in data['Meta Data'].items():
                        show_strings.extend([key, ": ", value, "\n"])
                    df_table = pd.DataFrame(data[f'{timeframe} Time Series']).T
                    table = tabulate(df_table, headers=list(df_table))
                    show_strings.append(table)

                # current quote
                elif action == "Current Quote":
                    data = self.client.get_current_quote(selected_symbol)
                    quote = data['Global Quote']
                    table = tabulate([list(quote.values())], headers=list(quote.keys()))
                    show_strings.append(table)

                # indicator results
                elif action == "Indicator Results":
                    data = self.client.get_indicators(selected_symbol)
                    for key, value in data['Meta Data'].items():
                        show_strings.extend([key, ": ", value, "\n"])
                    df_table = pd.DataFrame(data['Technical Analysis: SMA']).T
                    table = tabulate(df_table, headers=list(df_table))
                    show_strings.append(table)
                
                # show info to user
                show_strings = [str(s) for s in show_strings]
                enquiries.choose(''.join(show_strings), ['Select New Option...'])
