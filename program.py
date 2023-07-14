import pandas as pd
import functions as f
import tools as t
import urls as u

api_key = "67GDJTT1ZZGTTTN4"
ticker = u.ticker

print(t.MACDEXT())

# data_t = {'macd': t.MACDEXT(),
#         'stoch': t.STOCH(),
#         'ma': t.moving_average()}

# data_f = {'tckr': ticker, 'roic': f.ROIC(), 
#         'eqg': f.equity_growth(), 'eqg5': f.equity_growth_5(), 
#         'eps': f.EPS_growth(), 'eps5': f.EPS_growth_5,
#         'gpg': f.GP_growth(), 'gpg5': f.GP_growth_3,
#         'fcf': f.cash_flow_growth(), 'fcf5': f.cash_flow_growth_5()}

# print(data_f)