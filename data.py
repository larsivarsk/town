
import requests

api_key = "67GDJTT1ZZGTTTN4"
ticker = "NVDA"
keyword = "DNB"

earnings = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={api_key}'
overview = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={api_key}'
balance_sheet = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey={api_key}'
income = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}'
ticker_search = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={api_key}'

# request_earnings = requests.get(earnings)
# earnings_data = request_earnings.json()
# print(earnings_data)
# print("\nSKILLE\n")

# request_balance_sheet = requests.get(balance_sheet)
# balance_sheet_data = request_balance_sheet.json()
# print(balance_sheet_data)
# print("\nSKILLE\n")

request_income = requests.get(income)
income_data = request_income.json()
print(income_data)
print("\nSKILLE\n")

# request_search = requests.get(ticker_search)
# search_data = request_search.json()
# print(search_data)  
# print("\nSKILLE\n") 


#request_overview = requests.get(overview)
#overview_data = request_overview.json()
#print(overview_data)




#GROSS PROFIT DATA 
#----------------------------------------------

#Returns a list of the last 5 years of gross profit
#from oldest to newest
def gross_profit():
    gross_profit_list = []
    for data in income_data['annualReports']:
        gross_profit_list.append(float(data['grossProfit']))
    
    #FROM OLDEST TO NEWEST
    gross_profit_list.reverse()
    return gross_profit_list


#Returns a list of the last 5 years of gross profit
#growth data from oldest to newest
def GP_growth():
    print("GP_growth")
    gross_profit_list = gross_profit()
    
    gp_growth_list = []
    for i in range(0, len(gross_profit_list)-1):
        growth = (gross_profit_list[i+1]/gross_profit_list[i])-1
        gp_growth_list.append(round(growth,3))
    
    return gp_growth_list

print(GP_growth())
    

def GP_growth_5():
    print("GP_growth_5")
    data = gross_profit()
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

print(GP_growth_5())

def GP_growth_3():
    print("GP_growth_3")
    data = gross_profit()
    if len(data) < 3:
        return "-"
    return round(((data[2]/data[0])**0.333)-1,3)

print(GP_growth_3())


#ROIC DATA
#----------------------------------------------

#Returns a list of the last 10 years of ROIC
#data from oldest to newest
def ROIC():
    
    print("ROIC")
    
    income_list = []
    interest_expense_list = []
    tax_rate_list = []
    nopat_list = []
    equity_debt_list = []
    roic_list = []  
    
    for data in income_data['annualReports']:
        income_list.append(float(data['netIncomeFromContinuingOperations']))
        
        interest_expense_list.append(float(data['interestExpense']))
        
        rate = float(data['incomeTaxExpense'])/float(data['incomeBeforeTax'])
        tax_rate_list.append(rate)
        
    for data in balance_sheet_data['annualReports']:
        equity_debt = float(data['totalShareholderEquity']) + float(data['totalLiabilities'])
        equity_debt_list.append(equity_debt)
        
    for i in range(0, min(len(income_list), len(equity_debt_list))):
        nopat = income_list[i] + interest_expense_list[i]*(1-tax_rate_list[i])
        nopat_list.append(round(nopat,0))
    
    #FROM OLDEST TO NEWEST    
    equity_debt_list.reverse()
    nopat_list.reverse()
    
    for i in range(0, min(len(nopat_list), len(equity_debt_list))):
        roic = nopat_list[i]/equity_debt_list[i]
        roic_list.append(round(roic,3))
        
    return roic_list
        
    # print(tax_rate_list)
    # print(income_list)
    # print(interest_expense_list)
    # print(nopat_list)
    # print(equity_debt_list)
    # print(roic_list)
        
# ROIC()
#----------------------------------------------


#EPS DATA
#----------------------------------------------

#Returns a list of the last 10 years of EPS 
#data from oldest to newest
def EPS():
    eps_list = []

    for eps in earnings_data['annualEarnings']:
        eps_list.append(float(eps['reportedEPS']))
        
    eps_list_10 = eps_list[:10]
    
    #FROM OLDEST TO NEWEST
    eps_list_10.reverse()
    return eps_list_10

#Returns EPS growth over the last 10 years
def EPS_growth_10():
    print("EPS_growth_10")
    data = EPS()
    return round(((data[9]/data[0])**0.1)-1,3)

#Returns EPS growth over the last 5 years
def EPS_growth_5():
    print("EPS_growth_5")
    data = EPS()
    return round(((data[4]/data[0])**0.2)-1,3)

#Returns EPS growth over the last 3 years
def EPS_growth_3():
    print("EPS_growth_3")
    data = EPS()
    return round(((data[2]/data[0])**0.333)-1,3)

#Returns EPS growth over the last year (abundant?)
# def EPS_growth_1():
#     data = EPS()
#     return round(((data[1]/data[0])**1)-1,3)

#Returns a list over EPS growth year over year
def EPS_growth():
    print("EPS_growth")
    data = EPS()
    liste = []
    for i in range(0, len(data)-1):
        liste.append(round((data[i+1]/data[i])-1,3))
    
    return liste        
    

# print(EPS())
# print(EPS_growth_10())
# print(EPS_growth_5())
# print(EPS_growth_3())
# print(EPS_growth())
#----------------------------------------------


