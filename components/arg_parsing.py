import argparse

from typing import List

def parse_args(args: List[str]):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'api_key', 
        type=str, 
        help="API key for alphavantage.co; can be requested "
            "via https://www.alphavantage.co/support/#api-key"
    )
    return parser.parse_args(args)
