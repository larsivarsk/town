import urls as u
import apistckr as a

#MACDEXT
#MACD - the gauge of the water hose (requires Premium)
#When hist > 0 - bullish
#----------------------------------------------

#Fast EMA - 12 day EMA
#Slow EMA - 26 day EMA
#Signal - 9 day EMA of MACD
def MACDEXT():
    data = u.MACDEXT(a.ticker, a.api_key)['Technical Analysis: MACDEXT']
    
    hist = []
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
    data = u.STOCH(a.ticker, a.api_key)['Technical Analysis: STOCH']
    
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

#==============================================================================


#MOVING AVERAGE
#Using the simple moving average (SMA)
#When price > SMA - bullish
#----------------------------------------------

def moving_average():
    ma_data = u.SMA(a.ticker, a.api_key)['Technical Analysis: SMA']
    daily_data = u.daily(a.ticker, a.api_key)['Time Series (Daily)']
    
    ma = []
    da = []
    
    for d in ma_data:
        ma.append(float(ma_data[d]['SMA']))
        
    #FROM OLDEST TO NEWEST, last 100 records
    #of moving average
    ma = ma[:100]
    ma.reverse()
    
    for d in daily_data:
        da.append(float(daily_data[d]['4. close']))
    
    #FROM OLDEST TO NEWEST, last 100 records
    #of daily adjusted close
    da = da[:100]
    da.reverse()
        
    return ma, da

#==============================================================================    

        