import requests

#Used in functions
#==============================================================================

def earnings(ticker, api_key):
    earnings = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={api_key}'
    request_earnings = requests.get(earnings)
    earnings_data = request_earnings.json()
    return earnings_data

print(earnings('EQNR', '67GDJTT1ZZGTTTN4'))

def balance_sheet(ticker, api_key):
    balance_sheet = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey={api_key}'
    request_balance_sheet = requests.get(balance_sheet)
    balance_sheet_data = request_balance_sheet.json()
    return balance_sheet_data

# print(balance_sheet('AAPL', '67GDJTT1ZZGTTTN4'))

def income_statement(ticker, api_key):
    income = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}'
    request_income = requests.get(income)
    income_data = request_income.json()
    return income_data

# print(income_statement('AAPL', '67GDJTT1ZZGTTTN4'))

def cash_flow(ticker, api_key):
    cash_flow = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={api_key}'
    request_cash_flow = requests.get(cash_flow)
    cash_flow_data = request_cash_flow.json()
    return cash_flow_data

# print(cash_flow('AAPL', '67GDJTT1ZZGTTTN4'))

def ticker_search(ticker, api_key):
    ticker_search = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={api_key}'
    request_search = requests.get(ticker_search)
    search_data = request_search.json()
    return search_data

# print(ticker_search('AAPL', '67GDJTT1ZZGTTTN4'))

def overview(ticker, api_key):
    overview = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={api_key}'
    request_overview = requests.get(overview)
    overview_data = request_overview.json()
    return overview_data

# print(overview('AAPL', '67GDJTT1ZZGTTTN4'))

#Used in tools
#==============================================================================

def MACDEXT(ticker, api_key):
    MACDEXT = f"https://www.alphavantage.co/query?function=MACDEXT&symbol={ticker}&interval=daily&series_type=open&apikey={api_key}"
    request_MACDEXT = requests.get(MACDEXT)
    MACDEXT_data = request_MACDEXT.json()
    return MACDEXT_data

# print(MACDEXT('AAPL', '67GDJTT1ZZGTTTN4'))

def STOCH(ticker, api_key):
    STOCH = f"https://www.alphavantage.co/query?function=STOCH&symbol={ticker}&interval=daily&apikey={api_key}"
    request_STOCH = requests.get(STOCH)
    STOCH_data = request_STOCH.json()
    return STOCH_data

# print(STOCH('AAPL', '67GDJTT1ZZGTTTN4')

def SMA(ticker, api_key):
    sma = f"https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=open&apikey={api_key}"
    request_sma = requests.get(sma)
    sma_data = request_sma.json()
    return sma_data

# print(SMA('AAPL', '67GDJTT1ZZGTTTN4'))


#Used in other
#==============================================================================

def daily_adjusted(ticker, api_key):
    daily_adjusted = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}"
    request_daily_adjusted = requests.get(daily_adjusted)
    daily_adjusted_data = request_daily_adjusted.json()
    return daily_adjusted_data

# print(daily_adjusted('AAPL', '67GDJTT1ZZGTTTN4'))

def daily(ticker, api_key):
    daily = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"
    request_daily = requests.get(daily)
    daily_data = request_daily.json()
    return daily_data

# print(daily('AAPL', '67GDJTT1ZZGTTTN4'))

def monthly_adjusted(ticker, api_key):
    monthly_adjusted = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={ticker}&apikey={api_key}&outputsize=full"
    request_monthly_adjusted = requests.get(monthly_adjusted)
    monthly_adjusted_data = request_monthly_adjusted.json()
    return monthly_adjusted_data

# print(monthly_adjusted('AAPL', '67GDJTT1ZZGTTTN4'))

def monthly(ticker, api_key):
    monthly = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&apikey={api_key}&outputsize=full"
    request_monthly = requests.get(monthly)
    monthly_data = request_monthly.json()
    return monthly_data

# print(monthly('AAPL', '67GDJTT1ZZGTTTN4'))