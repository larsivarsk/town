import requests
import datetime


today = datetime.date.today()
api_key = "67GDJTT1ZZGTTTN4"
ticker = "MSFT"
keyword = "MSFT"

MACDEXT = f"https://www.alphavantage.co/query?function=MACDEXT&symbol={ticker}&interval=daily&series_type=open&apikey={api_key}"
request_MACDEXT = requests.get(MACDEXT)
MACDEXT_data = request_MACDEXT.json()
print(MACDEXT_data)

#MACDEXT
#MACD - the gauge of the water hose
#(requires Premium)
#----------------------------------------------

#Fast EMA - 12 day EMA
#Slow EMA - 26 day EMA
#Signal Line - 9 day EMA of MACD
def MACDEXT():
    data = MACDEXT_data['Technical Analysis: MACDEXT']
    buy = data

print(today)