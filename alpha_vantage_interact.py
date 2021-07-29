import sys

from typing import List

from components.arg_parsing import parse_args
from components.alpha_vantage_interface import AlphaVantageInterface


def main(args: List[str]):

    args = parse_args(args)
    alpha_vantage_interface = AlphaVantageInterface(args.api_key)
    alpha_vantage_interface.run_cli()


if __name__ == "__main__":

    main(sys.argv[1:])
