import requests
import datetime

timedelta = datetime.timedelta(days=181)
today = datetime.date.today()

api_key = "67GDJTT1ZZGTTTN4"
ticker = "MSFT"


# MACDEXT = f"https://www.alphavantage.co/query?function=MACDEXT&symbol={ticker}&interval=daily&series_type=open&apikey={api_key}"
# request_MACDEXT = requests.get(MACDEXT)
# MACDEXT_data = request_MACDEXT.json()
# print(MACDEXT_data)

# STOCH = f"https://www.alphavantage.co/query?function=STOCH&symbol={ticker}&interval=daily&apikey={api_key}"
# request_STOCH = requests.get(STOCH)
# STOCH_data = request_STOCH.json()
#print(STOCH_data)

sma = f"https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=open&apikey={api_key}"
request_sma = requests.get(sma)
sma_data = request_sma.json()
# print(sma_data)
# print('\nSKILLE\n')

daily_adjusted = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}"
request_daily_adjusted = requests.get(daily_adjusted)
daily_adjusted_data = request_daily_adjusted.json()
# print(daily_adjusted_data)

#MACDEXT
#MACD - the gauge of the water hose
#(requires Premium)
#----------------------------------------------

#Fast EMA - 12 day EMA
#Slow EMA - 26 day EMA
#Signal - 9 day EMA of MACD
def MACDEXT():
    print('MACDEXT')
    data = MACDEXT_data['Technical Analysis: MACDEXT']
    
    hist = []
    date = ''
    for d in data:
        hist.append(float(data[d]['MACD_Hist']))
    
    #FROM OLDEST TO NEWEST, last 100 records
    hist = hist[:100]
    hist.reverse()
    
    return hist

#==============================================================================


#STOCH
#Stochastic Oscillator
#When SlowK crosses above SlowD - bullish
#----------------------------------------------

#SlowD - 3 day SMA of SlowK
def STOCH():
    print('STOCH')
    data = STOCH_data['Technical Analysis: STOCH']
    
    slowk = []
    slowd = []
    
    for d in data:
        slowk.append(float(data[d]['SlowK']))
        slowd.append(float(data[d]['SlowD']))
    
    #FROM OLDEST TO NEWEST, last 100 records
    slowk = slowk[:100]
    slowk.reverse()
    slowd = slowd[:100]
    slowd.reverse()
    
    return slowk, slowd

#MOVING AVERAGE
#Using the simple moving average
#----------------------------------------------

def moving_average():
    print('MOVING AVERAGE')
    ma_data = sma_data['Technical Analysis: SMA']
    da_data = daily_adjusted_data['Time Series (Daily)']
    
    ma = []
    da = []
    
    for d in ma_data:
        ma.append(float(ma_data[d]['SMA']))
        
    #FROM OLDEST TO NEWEST, last 100 records
    ma = ma[:100]
    ma.reverse()
    
    for d in da_data:
        da.append(float(da_data[d]['5. adjusted close']))
    
    #FROM OLDEST TO NEWEST, last 100 records
    da = da[:100]
    da.reverse()
    
    return ma, da

print(moving_average())
    
    
        