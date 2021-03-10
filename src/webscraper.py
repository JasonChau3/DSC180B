import yfinance as yf
import bs4 as bs
import pickle
import requests
import pandas as pd
from src.getTickers import *
import os

from pandas_datareader import data as pdr


'''
This method gets all the data of the Dow Jones stock and SP500 stocks in the 
last 6 months, and saves all of those data, in the data folder under each of 
its respective folders as csv's
Returns: None
'''
def getData():
    yf.pdr_override()
    dow = save_dow_tickers()
        
    data = pdr.get_data_yahoo(dow,period = "6mo", group_by='ticker')


    #loops for each ticker and create a dataaframe out of it
    for tickers in dow:
        df= pd.DataFrame(data[tickers])
        #max min normalize each column
        df =(df-df.min())/(df.max()-df.min())
        df = df.iloc[1:]
        
        df['Date'] = df.index.format()

        df.to_csv('./data/dowJonesData/' +tickers +'.csv',index= False);

    sp500tic = save_sp500_tickers()
    data = pdr.get_data_yahoo(sp500tic,period = "6mo", group_by='ticker')

    #loops for each ticker and create a dataaframe out of it
    for tickers in sp500tic:
        df= pd.DataFrame(data[tickers])
        df = (df-df.min())/(df.max()-df.min())
        df = df.iloc[1:]
        df['Date'] = df.index.format()
        df.to_csv('./data/SP500Data/' +tickers +'.csv', index = False)

    tickerdf = pd.DataFrame(sp500tic,columns=['ticker'])


