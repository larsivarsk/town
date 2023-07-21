import pandas as pd
import functions as f
import tools as t
import urls as u
import apistckr as a

ticker = a.ticker
api_key = a.api_key


def run_functions():
    income_statement = u.income_statement(a.ticker, a.api_key)['annualReports']
    balance_sheet = u.balance_sheet(a.ticker, a.api_key)['annualReports']
    
    return

def run_tools():
    return