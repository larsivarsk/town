
#MACDEXT
#MACD - the gauge of the water hose (requires Premium)
#When hist > 0 - bullish
#----------------------------------------------

#Fast EMA - 12 day EMA
#Slow EMA - 26 day EMA
#Signal - 9 day EMA of MACD
def MACD(data):
    
    hist = []
    macd = []
    signal = []
    
    for d in data:
        hist.append(float(data[d]['MACD_Hist']))
        macd.append(float(data[d]['MACD']))
        signal.append(float(data[d]['MACD_Signal']))
    
    #FROM OLDEST TO NEWEST, last 100 records
    hist = hist[:100]
    hist.reverse()
    macd = macd[:100]
    macd.reverse()
    signal = signal[:100]
    signal.reverse()
    
    return hist, macd, signal

#==============================================================================


#STOCH
#Stochastic Oscillator
#When SlowK crosses above SlowD - bullish
#----------------------------------------------

#SlowD - 3 day SMA of SlowK
def STOCH(data):
    
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

def moving_average(ma_data, daily_data):
    
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
        
    return ma, da, da[-1]

#==============================================================================    

        