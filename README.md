# 2020-2021-CQA-Portfolio-Competition
This repository contains both a automatic investment challenge portfolio update application and in the future, a folder of some algorithmic trading strategies I am developing to improve our alpha. 

Automatic Investment Challenge Portfolio Update Application

As part of the CQA Investment Challenge I am competing in, there are many mostly risk-based compliance rules that our team must follow in order to not lose points in the rankings. The rules include:

-Limit on # of trades: There is a limit of 1,000 trades in the competition.

-Stocks only: Portfolios can ONLY invest in individual stocks on US exchanges. ETFs and
ETNs are not allowed. ADRs are allowed.

-Portfolio Size: Each team will initially manage a $2,000,000 long/short stock portfolio
with about $1,000,000 in long picks and $1,000,000 in short picks.

-Minimum # of stocks: The portfolio must always own AT LEAST 40 stocks on the long
side and 40 stocks on the short side.

-Minimum Stock Price for Buying: $5

-Minimum Stock Price for Shorting: $5

-Position Weight: The maximum position weight on both the long and short side is 5% of
the Value of the Fund. 

-Dollar Neutrality: Portfolios must remain dollar neutral with a ratio that is greater than
or equal to 0.9 and less than or equal to 1.1.

-Cash: Portfolios may not hold more than a 5% weight in cash

In order to solve the issue of making sure we are constantly complying with the CQA Investment Challenges rules and in order to recieve easy to access updates, I created an application that automatically scrapes, analyzes, and emails us relevant portfolio updates. The application first remotely webscrapes our trading platform for the relevant data using the StockTrakDataReader.py file. Next it, uses the "NonJupyterPCS.py" file (Non-Jupyter production version of the "PortfolioComplianceSystem.ipynb" file), to derive the necessary data from our scraped files, check the status of the portfolio performance and compliance wise, and finally to create a customized portfolio update including information about the portfolios performance and compliance statuses. Finally, the "GmailMessenger.py" file uses smtplib to send out an email to my team members and I containing the portfolio update created in the "NonJupyterPCS.py" file. Although I currently use crontab to automatically schedule this application everyday, I plan on deploying it on google cloud in the future so I do not have to run my computer remotely.

