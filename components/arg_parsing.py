import argparse

from typing import List
from argparse import Namespace

def parse_args(args: List[str]) -> Namespace:
    """
    Parses cli args for alpha_vantage_interact.

    Args:
        args (List[str]): The user supplied arguments.

    Returns:
        Namespace: argparse parsed args.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'api_key', 
        type=str, 
        help="API key for alphavantage.co; can be requested "
            "via https://www.alphavantage.co/support/#api-key"
    )
    return parser.parse_args(args)
