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

    #Lists of data
    roic = f.ROIC(income_statement, balance_sheet)
    equity_growth = f.equity_growth(balance_sheet)
    eps_growth = f.EPS_growth(earnings)
    gp_growth = f.GP_growth(income_statement)
    fcf = f.cash_flow_growth(ticker, api_key)
    
    #Pricing numbers
    growth_ratio = f.growth_ratio(earnings, balance_sheet)
    intrinsic_value = f.intrinsic_value(earnings, balance_sheet)
    mos = f.MOS(earnings, balance_sheet)
    
    ticker_dict = {'Return on Invested Capital': roic, 
                   'Equity Growth': equity_growth, 
                   'EPS Growth': eps_growth, 
                   'Gross Profit Growth': gp_growth, 
                   'Free Cash Flow Growth': fcf, 
                   'Growth Ratio': growth_ratio, 
                   'Intrinsic Value': intrinsic_value, 
                   'Margin of Safety': mos,
                   'Current P/E': 1,
                   'Current Price': 1}
                   
                       
    stock_dict[ticker] = ticker_dict
    
    

# print(run_functions())

def run_tools():
    
    x_data= []
    for i in range(0, 100):
        x_data.append(i)        

    #Figure and three subplots (1 row, 3 columns)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    #==============================================================================
    hist = t.MACDEXT()
    ax1.bar(x_data, hist, label='MACD', color='green')
    ax1.set_xlabel('Last 100 Days')
    ax1.set_ylabel('Value')
    ax1.set_title('MACD HISTOGRAM')
    ax1.legend()

    #==============================================================================
    slowk, slowd = t.STOCH()
    ax2.plot(x_data, slowk, label='slowK', color='blue')
    ax2.plot(x_data, slowd, label='slowD', color='red')
    
    buy_signals = []
    sell_signals = []

    for i in range(1, len(slowk)):
        if slowk[i] > slowd[i] and slowk[i - 1] <= slowd[i - 1]:
            #Buy signal (crossover of SlowK above SlowD)
            buy_signals.append(i)
        elif slowk[i] < slowd[i] and slowk[i - 1] >= slowd[i - 1]:
            # Sell signal (crossover of SlowK below SlowD)
            sell_signals.append(i)

    plt.scatter(buy_signals, [slowk[i-1] for i in buy_signals], marker='^', color='black', label='Buy Signal', zorder=5)
    plt.scatter(sell_signals, [slowk[i-1] for i in sell_signals], marker='v', color='black', label='Sell Signal', zorder=5)

    
    ax2.set_xlabel('Last 100 Days')
    ax2.set_ylabel('Value')
    ax2.set_title('STOCH')
    ax2.legend()

    #==============================================================================
    ma, da = t.moving_average()
    ax3.plot(x_data, ma, label='ma', color='green')
    ax3.plot(x_data, da, label='da', color='purple')
    
    buy_signals = []
    sell_signals = []

    for i in range(1, len(ma)):
        if da[i] > ma[i] and da[i - 1] <= ma[i - 1]:
            #Buy signal (crossover of Stock Price above Moving Average)
            buy_signals.append(i)
        elif da[i] < ma[i] and da[i - 1] >= ma[i - 1]:
            # Sell signal (crossover of Stock Price below Moving Average)
            sell_signals.append(i)

    plt.scatter(buy_signals, [da[i-1] for i in buy_signals], marker='^', color='black', label='Buy Signal', zorder=5)
    plt.scatter(sell_signals, [da[i-1] for i in sell_signals], marker='v', color='black', label='Sell Signal', zorder=5)

    
    ax3.set_xlabel('Last 100 Days')
    ax3.set_ylabel('Value')
    ax3.set_title('MOVING AVERAGE')
    ax3.legend()
    
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    
    