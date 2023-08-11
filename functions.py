
import requests
import urls as u


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
        if data['totalShareholderEquity'] != 'None':
            equity_list.append(float(data['totalShareholderEquity']))
        else:
            equity_list.append(1)
        
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
        if eps['reportedEPS'] != 'None':    
            eps_list.append(float(eps['reportedEPS']))
        else:
            eps_list.append(1)
        
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
        if data['grossProfit'] != 'None':
            gross_profit_list.append(float(data['grossProfit']))
        else:
            gross_profit_list.append(1)
    
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
def free_cash_flow(fcf):
    free_cash_flow_list = []
    
    for data in fcf:
        if data['operatingCashflow'] != 'None' and data['capitalExpenditures'] != 'None':
            operating_cash_flow = float(data['operatingCashflow'])
            capital_expenditure = float(data['capitalExpenditures'])
            free_cash_flow_list.append(operating_cash_flow - capital_expenditure)
        elif data['capitalExpenditures'] == 'None':
            free_cash_flow_list.append(float(data['operatingCashflow']))
        else:
            free_cash_flow_list.append(1)
    
    #FROM OLDEST TO NEWEST
    free_cash_flow_list.reverse()
    return free_cash_flow_list

#Returns a list of cash flow growth year over year
#for the last 5 years from oldest to newest
def cash_flow_growth(fcf):
    cash_flow = free_cash_flow(fcf)
    
    cash_flow_growth = []
    for i in range(0, len(cash_flow)-1):
        growth = (cash_flow[i+1]/cash_flow[i])-1
        cash_flow_growth.append(round(growth,3))
    return cash_flow_growth
        
#5 year growth rate of cash flow
def cash_flow_growth_5(fcf):
    data = free_cash_flow(fcf)
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of cash flow
def cash_flow_growth_3(fcf):
    data = free_cash_flow(fcf)
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================

#PRICING AND DEBT

#Returns average equity growth rate
def equity_growth_average(balance_sheet):
    data = equity_growth(balance_sheet)
    average = sum(data)/len(data)
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
        reported_EPS = eps['reportedEPS']
        if reported_EPS != 'None':
            trailing += float(reported_EPS)
        else:
            trailing += 0
        counter += 1
    return trailing

#Finds the stockprice for a given date
def stockprice_monthly(date, monthly_data):
    data = monthly_data
    for d in data:
        if d[0:7] == date[0:7]:
            return float(data[d]['5. adjusted close'])
    return 0

#Finds the historical P/E ratio
def historical_pe(earnings, monthly_data):
    pe_ratios = []
    data = monthly_data
    earnings = earnings['quarterlyEarnings']
    counter = 0
    end_year = int(list(data)[0][0:4]) - 10
    
    while int(earnings[counter]['reportedDate'][0:4]) >= end_year:
        
        date = earnings[counter]['reportedDate']
        stock_price = stockprice_monthly(date, data)
        
        # Calculate TTM EPS by summing EPS for the previous four quarters
        ttm_eps = sum(float(entry['reportedEPS']) if entry['reportedEPS'] != 'None' else 0 for entry in earnings[counter:counter+4])
        ttm_pe_ratio = stock_price / ttm_eps
        pe_ratios.append(ttm_pe_ratio)
        counter += 1

    average_pe = round(sum(pe_ratios)/len(pe_ratios), 3)
    
    return average_pe


#Returns the ratio between the eps growth and equity growth averages
def growth_ratio(balance_sheet, earnings):
    return EPS_growth_average(earnings)/equity_growth_average(balance_sheet)

#Sets default P/E ratio to 2*equity growth average
def default_pe(balance_sheet):
    return equity_growth_average(balance_sheet)*2*100

#Chooses the lowest P/E ratio between the historical and default P/E
def choose_pe(balance_sheet, earnings, monthly_data):
    if historical_pe(earnings, monthly_data) < default_pe(balance_sheet) or default_pe(balance_sheet) < 0:
        return historical_pe(earnings, monthly_data)
    return default_pe(balance_sheet)

#Returns the intrinsic value of the stock
def intrinsic_value(balance_sheet, earnings, monthly_data):
    future_eps = trailing_EPS(earnings)*(1+equity_growth_average(balance_sheet))**10
    pe = choose_pe(balance_sheet, earnings, monthly_data)
    return round(future_eps*pe/4, 3)

#Returns the margin of safety on the stock
def MOS(balance_sheet, earnings, monthly_data):
    return round(intrinsic_value(balance_sheet, earnings, monthly_data)/2, 3)

#Returns the ratio between free cash flow to long term debt 
def cf_to_debt(balance_sheet, cash_flow):
    debt = float(balance_sheet[0]['longTermDebtNoncurrent'])
    fcf = float(cash_flow[0]['operatingCashflow']) - float(cash_flow[0]['capitalExpenditures'])
    if debt != 'None' and fcf != 'None':
        return round(fcf/debt, 3)
    return 0
