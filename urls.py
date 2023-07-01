import requests

api_key = "67GDJTT1ZZGTTTN4"
ticker = input("Enter ticker: ").upper()
keyword = ticker

#Used in functions
#==============================================================================

def earnings():
    earnings = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={api_key}'
    request_earnings = requests.get(earnings)
    earnings_data = request_earnings.json()
    return earnings_data

def balance_sheet():
    balance_sheet = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey={api_key}'
    request_balance_sheet = requests.get(balance_sheet)
    balance_sheet_data = request_balance_sheet.json()
    return balance_sheet_data

def income_statement():
    income = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}'
    request_income = requests.get(income)
    income_data = request_income.json()
    return income_data

def cash_flow():
    cash_flow = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={api_key}'
    request_cash_flow = requests.get(cash_flow)
    cash_flow_data = request_cash_flow.json()
    return cash_flow_data

def ticker_search(keyword):
    ticker_search = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={api_key}'
    request_search = requests.get(ticker_search)
    search_data = request_search.json()
    return search_data

def overview():
    overview = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={api_key}'
    request_overview = requests.get(overview)
    overview_data = request_overview.json()
    return overview_data


    #Used in tools
    #==============================================================================

def MACDEXT():
    MACDEXT = f"https://www.alphavantage.co/query?function=MACDEXT&symbol={ticker}&interval=daily&series_type=open&apikey={api_key}"
    request_MACDEXT = requests.get(MACDEXT)
    MACDEXT_data = request_MACDEXT.json()
    return MACDEXT_data

def STOCH():
    STOCH = f"https://www.alphavantage.co/query?function=STOCH&symbol={ticker}&interval=daily&apikey={api_key}"
    request_STOCH = requests.get(STOCH)
    STOCH_data = request_STOCH.json()
    return STOCH_data

def SMA():
    sma = f"https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=open&apikey={api_key}"
    request_sma = requests.get(sma)
    sma_data = request_sma.json()
    return sma_data

def daily_adjusted():
    daily_adjusted = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}"
    request_daily_adjusted = requests.get(daily_adjusted)
    daily_adjusted_data = request_daily_adjusted.json()
    return daily_adjusted_data