# colmore-test
COLMORE PYTHON DEVELOPER TEST

CLI 
- user provide API key
- search and display companies

Please build a command line interface or simple flask front-end site that support following features:

1. User provides its own API key that is remembered for the session

2. User can search specific company using
https://www.alphavantage.co/documentation/#symbolsearch and display results that match selection criteria in select list, e.g:

3. User can select a company and have one of following options for it:
- display additional details in grid as:
symbol, name, type, region, marketOpen, marketClose, timezone, currency, matchScore
- display historical prices on specific timeframes:
intraday as 5m, 15m,.., daily or weekly or monthly (select two):
https://www.alphavantage.co/documentation/#intraday , https://www.alphavantage.co/documentation/#daily https://www.alphavantage.co/documentation/#weekly
https://www.alphavantage.co/documentation/#monthly
- display current quote:
https://www.alphavantage.co/documentation/#latestprice
- indicator results for it in grid:
https://www.alphavantage.co/documentation/#technical-indicators