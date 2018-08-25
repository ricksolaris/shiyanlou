import pandas_datareader.data as web
import pandas as pd
import datetime
import numpy as np

def alibaba():

    start = datetime.datetime(2017,1,1)
    end = datetime.datetime(2017,12,31)

    df_year_2017 = web.DataReader('BABA', 'yahoo', start, end)

    year_2017_close = df_year_2017.Close
    log_change = np.log(year_2017_close) - np.log(year_2017_close.shift(1))

    rise = (log_change > 0).sum()
    fall = (log_change < 0).sum()

    return rise, fall
alibaba()