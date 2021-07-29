

import sys

import enquiries


def select_match(matches):
    
    symbols = [item['1. symbol'] for item in matches]
    names = [item['2. name'] for item in matches]

    options = [f"{symbol} - {name}" for symbol, name in zip(symbols, names)]
    options.append('Search again...')
    selected = enquiries.choose("Select", options)
    symbol = selected.split(" ")[0]

    try:
        selected_index = symbols.index(symbol)
    except ValueError:
        selected_index = -1
    
    return selected_index
