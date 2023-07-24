
import requests
import urls as u
import apistckr as a


#ROIC DATA
#----------------------------------------------

#Returns list of the last 5 years of ROIC data from 
#oldest to newest
def ROIC(income_statement, balance_sheet):
        
    income_list = []
    interest_expense_list = []
    tax_rate_list = []
    equity_debt_list = []
    roic_list = []  
    
    for data in income_statement:
        income_list.append(float(data['netIncomeFromContinuingOperations']))
        interest_expense = data['interestExpense']
        if interest_expense != 'None':
            interest_expense_list.append(float(interest_expense))
        else:
            interest_expense_list.append(0)
            
        
        tax_rate = float(data['incomeTaxExpense'])/float(data['incomeBeforeTax'])
        tax_rate_list.append(tax_rate)
            
    for data in balance_sheet:
        equity_debt = float(data['totalShareholderEquity']) + float(data['totalLiabilities'])
        equity_debt_list.append(equity_debt)
                
    for i in range(0, min(len(income_list), len(equity_debt_list))):
        nopat = income_list[i] + interest_expense_list[i]*(1-tax_rate_list[i])
        roic = nopat/equity_debt_list[i]
        roic_list.append(round(roic,3))
            
    #FROM OLDEST TO NEWEST        
    roic_list.reverse()
    
    return roic_list

#==============================================================================


#EQUITY DATA 
#----------------------------------------------

#List of the last 5 years of equity data from
#oldest to newest
def equity(balance_sheet):
    equity_list = []
    for data in balance_sheet:
        equity_list.append(float(data['totalShareholderEquity']))
        
    #FROM OLDEST TO NEWEST
    equity_list.reverse()
    return equity_list

#Growth rate of equity year over year for the
#last 5 years from oldest to newest
def equity_growth(balance_sheet):
    equity_list = equity(balance_sheet)
    
    equity_growth_list = []
    for i in range(0, len(equity_list)-1):
        growth = (equity_list[i+1]/equity_list[i])-1
        equity_growth_list.append(round(growth,3))
        
    return equity_growth_list


# print(equity_growth(u.balance_sheet(a.ticker, a.api_key)['annualReports']))
# print(equity_growth_average(u.balance_sheet(a.ticker, a.api_key)['annualReports']))

#5 year growth rate of equity
def equity_growth_5(balance_sheet):
    data = equity(balance_sheet)
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of equity
def equity_growth_3(balance_sheet):
    data = equity(balance_sheet)
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================


#EPS DATA
#----------------------------------------------

#List of the last 10 years of EPS 
#data from oldest to newest
def EPS(earnings):
    eps_list = []

    for eps in earnings['annualEarnings']:
        eps_list.append(float(eps['reportedEPS']))
        
    eps_list_10 = eps_list[:10]
    
    #FROM OLDEST TO NEWEST
    eps_list_10.reverse()
    return eps_list_10

#Returns a list of EPS growth year over year
#for the last 10 years from oldest to newest
def EPS_growth(earnings):
    data = EPS(earnings)
    liste = []
    for i in range(0, len(data)-1):
        liste.append(round((data[i+1]/data[i])-1,3))
    return liste   

#10 year growth rate of EPS
def EPS_growth_10(earnings):
    data = EPS(earnings)
    return round(((data[9]/data[0])**0.1)-1,3)

#5 year growth rate of EPS
def EPS_growth_5(earnings):
    data = EPS(earnings)
    return round(((data[9]/data[6])**0.2)-1,3)

#3 year growth rate of EPS
def EPS_growth_3(earnings):
    data = EPS(earnings)
    return round(((data[4]/data[2])**0.333)-1,3)     

#==============================================================================


#GROSS PROFIT DATA 
#----------------------------------------------

#List of the last 5 years of gross profit data
#from oldest to newest
def gross_profit(income_statement):
    gross_profit_list = []
    for data in income_statement:
        gross_profit_list.append(float(data['grossProfit']))
    
    #FROM OLDEST TO NEWEST
    gross_profit_list.reverse()
    return gross_profit_list

#Returns a list over gross profit growth year over year 
#for the last 5 years from oldest to newest
def GP_growth(income_statement):
    gross_profit_list = gross_profit(income_statement)
    
    gp_growth_list = []
    for i in range(0, len(gross_profit_list)-1):
        growth = (gross_profit_list[i+1]/gross_profit_list[i])-1
        gp_growth_list.append(round(growth,3))
    
    return gp_growth_list
    
#5 year growth rate of gross profit
def GP_growth_5(income_statement):
    data = gross_profit(income_statement)
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of gross profit
def GP_growth_3(income_statement):
    data = gross_profit(income_statement)
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================


#CASH FLOW DATA
#----------------------------------------------

#List of the last 5 years of cash flow data from
#oldest to newest
def free_cash_flow(ticker, api_key):
    free_cash_flow_list = []
    
    for data in u.cash_flow(ticker, api_key)['annualReports']:
        operating_cash_flow = float(data['operatingCashflow'])
        capital_expenditure = float(data['capitalExpenditures'])
        free_cash_flow_list.append(operating_cash_flow - capital_expenditure)
    
    #FROM OLDEST TO NEWEST
    free_cash_flow_list.reverse()
    return free_cash_flow_list

#Returns a list of cash flow growth year over year
#for the last 5 years from oldest to newest
def cash_flow_growth(ticker, api_key):
    cash_flow = free_cash_flow(ticker, api_key)
    
    cash_flow_growth = []
    for i in range(0, len(cash_flow)-1):
        growth = (cash_flow[i+1]/cash_flow[i])-1
        cash_flow_growth.append(round(growth,3))
    return cash_flow_growth
        
#5 year growth rate of cash flow
def cash_flow_growth_5(ticker, api_key):
    data = free_cash_flow(ticker, api_key)
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of cash flow
def cash_flow_growth_3(ticker, api_key):
    data = free_cash_flow()
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================

#PRICING

#Returns average equity growth rate
def equity_growth_average(balance_sheet):
    number = 0
    data = equity_growth(balance_sheet)
    for growth in data:
        number += growth
    average = number/len(data)
    return round(average, 3)

#Returns average EPS of the last 10 years
def EPS_growth_average(earnings):
    number = 0
    data = EPS_growth(earnings)
    for growth in data:
        number += growth
    
    average = number/len(data)
    return round(average, 3)

#Returns the trailing EPS of the last 4 quarters
def trailing_EPS(earnings):
    trailing = 0
    counter = 0
    for eps in earnings['quarterlyEarnings']:
        if counter == 4:
            break  
        trailing += float(eps['reportedEPS'])
        counter += 1
    return trailing


def stockprice_monthly(date, monthly_data):
    data = monthly_data
    for d in data:
        if d[0:7] == date[0:7]:
            return float(data[d]['4. close'])
    return 0


def historical_pe(earnings, ticker, api_key):
    pe_ratios = []
    monthly_data = u.monthly(ticker, api_key)['Monthly Time Series']
    earnings = earnings['quarterlyEarnings']
    counter = 0
    end_year = int(list(monthly_data)[0][0:4]) - 10
    
    while int(earnings[counter]['reportedDate'][0:4]) >= end_year:
        
        date = earnings[counter]['reportedDate']
        stock_price = stockprice_monthly(date, monthly_data)
        counter += 1
        
        # print(stock_price)
        
        # Calculate TTM EPS by summing EPS for the previous four quarters
        ttm_eps = sum(float(entry['reportedEPS']) for entry in earnings[counter:counter+4])
        ttm_pe_ratio = stock_price / ttm_eps
        pe_ratios.append(ttm_pe_ratio)

    return pe_ratios/len(pe_ratios)
    
    
    # # print(earnings)
    # for d in monthly_data:
    #     date = d
                
    #     if int(date[0:4]) < end_year:
    #         break
        
    #     # print(earnings[counter]['reportedDate'])
    #     # print(earnings[counter]['reportedEPS'])
        
    #     for entry in earnings[counter:counter+4]:
    #         print(entry['reportedEPS'])
        
    #     counter += 1
    #     stock_price = stockprice_monthly(date, monthly_data)
    #     # print(stock_price)
    #     # Check if counter is greater than or equal to 4 to calculate TTM EPS
    #     if counter >= 4:
    #         # Calculate TTM EPS by summing EPS for the previous four quarters
    #         ttm_eps = sum(float(entry['reportedEPS']) for entry in earnings[counter-4:counter])
    #         if ttm_eps > 0 and stock_price > 0:
    #             ttm_pe_ratio = stock_price / ttm_eps
    #             pe_ratios.append(ttm_pe_ratio)

    # return pe_ratios


historical_pe()
 
def growth_ratio(earnings, balance_sheet):
    return EPS_growth_average(earnings)/equity_growth_average(balance_sheet)

def default_pe(balance_sheet):
    return equity_growth_average(balance_sheet)*2*100

def choose_pe(balance_sheet):
    if historical_pe() > default_pe(balance_sheet):
        return historical_pe()
    return default_pe()

def intrinsic_value(earnings, balance_sheet):
    future_eps = trailing_EPS(earnings)*equity_growth_average(balance_sheet)**10
    pe = choose_pe(balance_sheet)
    return round(future_eps*pe/4, 3)

def MOS(earnings, balance_sheet):
    return round(intrinsic_value(earnings, balance_sheet)/2, 3)