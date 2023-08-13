# town

This program is a tool for doing fundamental analysis, inspired by Phil Town's book "Rule #1". It is meant to be used as a complement to other research, and 
does not work as a stock picking program.

### Main takeaways:
- Finds and returns ROIC over the last 5 years.
- Finds and returns key growth rates such as equity-, EPS-, gross profit- and free cash flow growth over a period of 5-10 years.
- Finds and returns pricing of a company and the margin of safety based on the approach in "Rule #1".
- Also deliver other metrics involving debt, earnings, assets, equity and so on - an overview.
- Graphs MACD, stochastic oscillator and moving average over the last 100 days.

### Weaknesses:
- Pricing requires the key growth rates to be stable and the annual yield to be 15%. Volatile companys with varying results are not this strategy's main target, and consequently, innacurate when assesing such companies. 
- The tool is slow because of the API cost. The free version allows 5 requests/min and 100 requests/day. The program uses 10 requests in one run, so a delay between the 5 first and 5 last calls had to be added.
- Optimally, all the growth rates would have covered the last 10 years. However, only the EPS growth rate covers the last 10 years, the others were not shown (if you know how to fix this, please let me know).
- The program mainly covers US companies, and often delivers incomplete information on companies outside the US, sometimes leading the program to crash. 

### Run the project (as of 08.14.2023):
- Type the following in your terminal:
```
python -m pip install -U pip
python -m pip install -U matplotlib
```
- Go to the 'apisticker.py' module and replace the 'api_key' variable with your own key. A key can be collected at https://www.alphavantage.co/support/#api-key
- Enter the filepath/directory where the program is saved in your terminal.
- Type the following in your terminal:
```
python -u program.py
```
- The program should now be running, and you can type the ticker of the company you want information on in your terminal.
- CTRL + C shuts the program down, also closing the open window showing the graphs.

##### DOCUMENTATION: https://www.alphavantage.co/documentation/
