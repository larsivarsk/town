
import requests
import urls as u


#ROIC DATA
#----------------------------------------------

#Returns list of the last 5 years of ROIC data from 
#oldest to newest
def ROIC():
    
    print("ROIC")
    
    income_list = []
    interest_expense_list = []
    tax_rate_list = []
    equity_debt_list = []
    roic_list = []  
    
    for data in u.income_statement()['annualReports']:
        income_list.append(float(data['netIncomeFromContinuingOperations']))
        interest_expense = data['interestExpense']
        if interest_expense != 'None':
            interest_expense_list.append(float(interest_expense))
        else:
            interest_expense_list.append(0)
            
        
        tax_rate = float(data['incomeTaxExpense'])/float(data['incomeBeforeTax'])
        tax_rate_list.append(tax_rate)
            
    for data in u.balance_sheet()['annualReports']:
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


#EQUiTY DATA 
#----------------------------------------------

#List of the last 5 years of equity data from
#oldest to newest
def equity():
    equity_list = []
    for data in u.balance_sheet()['annualReports']:
        equity_list.append(float(data['totalShareholderEquity']))
        
    #FROM OLDEST TO NEWEST
    equity_list.reverse()
    return equity_list

#Growth rate of equity year over year for the
#last 5 years from oldest to newest
def equity_growth():
    print("Equity growth")
    equity_list = equity()
    print(equity_list)
    
    equity_growth_list = []
    for i in range(0, len(equity_list)-1):
        growth = (equity_list[i+1]/equity_list[i])-1
        equity_growth_list.append(round(growth,3))
        
    return equity_growth_list

#5 year growth rate of equity
def equity_growth_5():
    print("equity_growth_5")
    data = equity()
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of equity
def equity_growth_3():
    print("equity_growth_3")
    data = equity()
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================


#EPS DATA
#----------------------------------------------

#List of the last 10 years of EPS 
#data from oldest to newest
def EPS():
    eps_list = []

    for eps in u.earnings()['annualEarnings']:
        eps_list.append(float(eps['reportedEPS']))
        
    eps_list_10 = eps_list[:10]
    
    #FROM OLDEST TO NEWEST
    eps_list_10.reverse()
    return eps_list_10

#10 year growth rate of EPS
def EPS_growth_10():
    print("EPS_growth_10")
    data = EPS()
    return round(((data[9]/data[0])**0.1)-1,3)

#5 year growth rate of EPS
def EPS_growth_5():
    print("EPS_growth_5")
    data = EPS()
    return round(((data[9]/data[6])**0.2)-1,3)

#3 year growth rate of EPS
def EPS_growth_3():
    print("EPS_growth_3")
    data = EPS()
    return round(((data[4]/data[2])**0.333)-1,3)

#Returns a list of EPS growth year over year
#for the last 10 years from oldest to newest
def EPS_growth():
    print("EPS growth")
    data = EPS()
    liste = []
    for i in range(0, len(data)-1):
        liste.append(round((data[i+1]/data[i])-1,3))
    
    return liste        
    
#==============================================================================


#GROSS PROFIT DATA 
#----------------------------------------------

#List of the last 5 years of gross profit data
#from oldest to newest
def gross_profit():
    gross_profit_list = []
    for data in u.income_statement()['annualReports']:
        gross_profit_list.append(float(data['grossProfit']))
    
    #FROM OLDEST TO NEWEST
    gross_profit_list.reverse()
    return gross_profit_list

#Returns a list over gross profit growth year over year 
#for the last 5 years from oldest to newest
def GP_growth():
    print("GP growth")
    gross_profit_list = gross_profit()
    
    gp_growth_list = []
    for i in range(0, len(gross_profit_list)-1):
        growth = (gross_profit_list[i+1]/gross_profit_list[i])-1
        gp_growth_list.append(round(growth,3))
    
    return gp_growth_list
    
#5 year growth rate of gross profit
def GP_growth_5():
    print("GP_growth_5")
    data = gross_profit()
    if len(data) < 5:
        return "-"
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of gross profit
def GP_growth_3():
    print("GP_growth_3")
    data = gross_profit()
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================


#CASH FLOW DATA
#----------------------------------------------

#List of the last 5 years of cash flow data from
#oldest to newest
def free_cash_flow():
    free_cash_flow_list = []
    
    for data in u.cash_flow()['annualReports']:
        operating_cash_flow = float(data['operatingCashflow'])
        capital_expenditure = float(data['capitalExpenditures'])
        free_cash_flow_list.append(operating_cash_flow - capital_expenditure)
    
    #FROM OLDEST TO NEWEST
    free_cash_flow_list.reverse()
    return free_cash_flow_list

#Returns a list of cash flow growth year over year
#for the last 5 years from oldest to newest
def cash_flow_growth():
    print("Cash flow growth")
    cash_flow = free_cash_flow()
    
    cash_flow_growth = []
    for i in range(0, len(cash_flow)-1):
        growth = (cash_flow[i+1]/cash_flow[i])-1
        cash_flow_growth.append(round(growth,3))
    return cash_flow_growth
        
#5 year growth rate of cash flow
def cash_flow_growth_5():
    print("cash_flow_growth_5")
    data = free_cash_flow()
    if len(data) < 5:
        return "-"
    print(data)
    return round(((data[4]/data[0])**0.2)-1,3)

#3 year growth rate of cash flow
def cash_flow_growth_3():
    print("cash_flow_growth_3")
    data = free_cash_flow()
    if len(data) < 3:
        return "-"
    return round(((data[4]/data[2])**0.333)-1,3)

#==============================================================================