#!/Applications/miniconda3/envs/CQAChallenge/bin/python
#Imports
import pandas as pd
import numpy as np
from datetime import datetime
import os
import glob
from StockTrakDataReader import portfolio_value
import config

#Get current date/time
now = datetime.now()
current_time = now.strftime("%m/%d/%Y, %-I:%M %p")
print(current_time)

#Turn portfolio value in integer for calculations
portfolio_value = portfolio_value.replace(',','')
totalportfoliovalue = float(portfolio_value[1:])
print(totalportfoliovalue)

#Create message/update
portfolioupdate = 'Dutchmen Alpha Fund Portfolio Update\n\n' + current_time + '\n\n'

#Load in portfolio and view head
datafolder = glob.iglob(config.portfoliodatafolder)
latestportfolio = max(datafolder, key=os.path.getctime)
portfolio = pd.read_csv(latestportfolio, index_col=False)
print(portfolio.head())

#Identify short tickets
shorttickers = portfolio[portfolio['Quantity']<0]

#Identify long tickers
longtickers = portfolio[portfolio['Quantity']>0]

#Identify stocks purchased below the minimum
stockspurchasedbelowmin = portfolio[(portfolio['PricePaid']<5) & (portfolio['Quantity']>0)]

#Identify stocks shorted below the minimum
stocksshortedbelowmin = portfolio[(portfolio['PricePaid']<5) & (portfolio['Quantity']<0)]

#Add the total portfolio value to the update
portfolioupdate += ('The total portfolio value is currently: $' + str(round(totalportfoliovalue,2)) + '\n\n')

#Calculate position weights
portfolio['positionweight'] = portfolio['MarketValue']/totalportfoliovalue

#Identify overweight stocks
overweightstocks = portfolio[portfolio['positionweight']>=.05]
verycloseoverweightstocks = portfolio[(portfolio['positionweight']>=.045) & (portfolio['positionweight']<.05)]
closeoverweightstocks = portfolio[(portfolio['positionweight']>=.04) & (portfolio['positionweight']<.045)]
print(overweightstocks)

#Calculate dollar neutrality rate
dollarneutralityratio = longtickers['MarketValue'].sum()/shorttickers['MarketValue'].sum()

#Add short tickers count to update
if len(shorttickers.index) < 40:
    portfolioupdate += ('There are not enough short tickers in the portfolio. There are only ' + str(len(shorttickers)) + ':\n\n' + str(shorttickers[['Symbol','Quantity']])+'\n\n')
else:
    portfolioupdate += ('The number of short tickers is good!. There are: ' + str(len(shorttickers)) + '\n\n')

#Add long tickers count to update
if len(longtickers.index) < 40:
    portfolioupdate += ('There are not enough long tickers in the portfolio. There are only ' + str(len(longtickers)) + ':\n\n'+str(longtickers[['Symbol','Quantity']])+'\n\n')
else:
    portfolioupdate += ('The number of long tickers is good!. There are: ' + str(len(longtickers))+ '\n\n')

#Add stocks purchased below min to update
if len(stockspurchasedbelowmin.index)>0:
    portfolioupdate += ('There are stocks that were purchased below the minimum price for buying of $5:\n\n'+str(stockspurchasedbelowmin[['Symbol','Description','PricePaid']])+'\n\n')
else:
    portfolioupdate += ('No holdings in the portfolio were purchased below the minimum of $5\n\n')

#Add stocks shorted below min to update
if len(stocksshortedbelowmin.index)>0:
    portfolioupdate += ('There are stocks that were shorted below the minimum price for shorting of $5:\n\n'+str(stocksshortedbelowmin[['Symbol','Description','PricePaid']])+'\n\n')
else:
    portfolioupdate += ('No holdings in the portfolio were shorted below the minimum of $5\n\n')

#Add dollar neutrality ratio to update
if dollarneutralityratio < .9 or dollarneutralityratio > 1.1:
    portfolioupdate += ('The portfolio dollar neutrality ratio is out of balance!. Current ratio is: '+str(round(dollarneutralityratio,4))+'\n\n')
else:
    portfolioupdate += ('The portfolio dollar neutrality ratio is in balance!. Current ratio is: ' + str(round(dollarneutralityratio,4))+'\n\n')

#Distribution of porfolio weights
welldistributed = True
if len(overweightstocks.index) > 0:
    portfolioupdate += ('There are overweight stocks with weights over the max of 5%:\n\n'+str(overweightstocks[['Symbol','positionweight']])+"\n\n")
    welldistributed = False
if len(verycloseoverweightstocks.index) > 0:
    portfolioupdate += ('There are stocks very close to overweight with weights over 4.5%:\n\n'+str(verycloseoverweightstocks[['Symbol','positionweight']])+"\n\n")
    welldistributed = False
if len(closeoverweightstocks.index) > 0:
    portfolioupdate += ('There are stocks close to overweight with weights over 4%. Keep an eye on them:\n\n'+str(closeoverweightstocks[['Symbol','positionweight']])+"\n\n")
    welldistributed = False
if welldistributed:
    portfolioupdate += ('Portfolio weights are well-distributed!')

#Define function to return update
def returnportfolioupdate():
    print(portfolioupdate)
returnportfolioupdate()


