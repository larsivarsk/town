import functions as f
import tools as t
import urls as u
import apistckr as a
import matplotlib.pyplot as plt

ticker = a.ticker
api_key = a.api_key
stock_dict = {}


def run_functions(ticker, api_key):
    earnings = u.earnings(ticker, api_key)
    balance_sheet = u.balance_sheet(ticker, api_key)['annualReports']
    income_statement = u.income_statement(ticker, api_key)['annualReports']
    cash_flow = u.cash_flow(ticker, api_key)['annualReports']
    monthly_adjusted = u.monthly_adjusted(ticker, api_key)['Monthly Adjusted Time Series']
    
        
    #Lists of data
    roic = f.ROIC(income_statement, balance_sheet)
    equity_growth = f.equity_growth(balance_sheet)
    eps_growth = f.EPS_growth(earnings)
    gp_growth = f.GP_growth(income_statement)
    fcf_growth = f.cash_flow_growth(cash_flow)
    fcf_debt = f.cf_to_debt(balance_sheet, cash_flow)    
    
    #Pricing numbers
    growth_ratio = f.growth_ratio(balance_sheet, earnings)
    intrinsic_value = f.intrinsic_value(balance_sheet, earnings, monthly_adjusted)
    mos = f.MOS(balance_sheet, earnings, monthly_adjusted)
    
    ticker_dict = {'Return on Invested Capital': roic, 
                   'Equity Growth': equity_growth, 
                   'EPS Growth': eps_growth, 
                   'Gross Profit Growth': gp_growth, 
                   'Free Cash Flow Growth': fcf_growth, 
                   'EPS growth/Equity growth': growth_ratio, 
                   'Intrinsic Value': intrinsic_value, 
                   'Margin of Safety': mos,
                   'Current P/E': 1,
                   'Current Price': 1,
                   'FCF/Debt': fcf_debt}
                   
    for key, value in ticker_dict.items():
        print(f'{key}: {value}')
    
    

# run_functions(ticker, api_key)

def run_tools(ticker, api_key):
    macd_data = u.MACDEXT(ticker, api_key)['Technical Analysis: MACDEXT']
    stoch_data = u.STOCH(ticker, api_key)['Technical Analysis: STOCH']
    ma_data = u.SMA(ticker, api_key)['Technical Analysis: SMA']
    daily_data = u.daily(ticker, api_key)['Time Series (Daily)']
    
    #100 days of data
    x_data= []
    for i in range(0, 100):
        x_data.append(i)        

    #Figure and three subplots (1 row, 3 columns)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    #==============================================================================
    hist = t.MACDEXT(macd_data)
    ax1.bar(x_data, hist, label='MACD', color='green')
    ax1.set_xlabel('Last 100 Days')
    ax1.set_ylabel('Value')
    ax1.set_title('MACD HISTOGRAM')
    ax1.legend()

    #==============================================================================
    slowk, slowd = t.STOCH(stoch_data)
    ax2.plot(x_data, slowk, label='slowK', color='blue')
    ax2.plot(x_data, slowd, label='slowD', color='red')

    buy_signals_s = []
    sell_signals_s = []

    for i in range(1, len(slowk)):
        if slowk[i] > slowd[i] and slowk[i - 1] <= slowd[i - 1]:
            # Buy signal (crossover of SlowK above SlowD)
            buy_signals_s.append(i)
        elif slowk[i] < slowd[i] and slowk[i - 1] >= slowd[i - 1]:
            # Sell signal (crossover of SlowK below SlowD)
            sell_signals_s.append(i)

    # Use ax2.scatter to add scatter plots to the second subplot (ax2)
    ax2.scatter(buy_signals_s, [slowk[i-1] for i in buy_signals_s], marker='^', color='black', label='Buy Signal_s', zorder=5)
    ax2.scatter(sell_signals_s, [slowk[i-1] for i in sell_signals_s], marker='v', color='black', label='Sell Signal_s', zorder=5)

    ax2.set_xlabel('Last 100 Days')
    ax2.set_ylabel('Value')
    ax2.set_title('STOCH')
    ax2.legend()

    #==============================================================================
    ma, da, today_close = t.moving_average(ma_data, daily_data)
    ax3.plot(x_data, ma, label='ma', color='green')
    ax3.plot(x_data, da, label='da', color='purple')
    
    buy_signals_m = []
    sell_signals_m = []

    for i in range(1, len(ma)):
        if da[i] > ma[i] and da[i - 1] <= ma[i - 1]:
            #Buy signal (crossover of Stock Price above Moving Average)
            buy_signals_m.append(i)
        elif da[i] < ma[i] and da[i - 1] >= ma[i - 1]:
            # Sell signal (crossover of Stock Price below Moving Average)
            sell_signals_m.append(i)

    plt.scatter(buy_signals_m, [da[i-1] for i in buy_signals_m], marker='^', color='black', label='Buy Signal_m', zorder=5)
    plt.scatter(sell_signals_m, [da[i-1] for i in sell_signals_m], marker='v', color='black', label='Sell Signal_m', zorder=5)

    
    ax3.set_xlabel(f'Today\'s Close: {today_close}; Signal:')
    ax3.set_ylabel('Value')
    ax3.set_title('MOVING AVERAGE')
    ax3.legend()
    
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    
    
# run_tools(ticker, api_key)
    
    