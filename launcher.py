# %%
import pandas as pd
import matplotlib.pyplot as plt
from QuantCore.QuantLib import GBM, HistoricalParametersCalcualtor
from Oracle.Oracle import Chainlink

# %%

# get todays price from Chainlink oracle
oracle = Chainlink()
sInitial = oracle.getLatestPrice('ETHUSD')

# get historical prices from chainlink oracle
historicalTimeSeries = oracle.getHistoricalPrices(
    'ETHUSD', 'startDate', 'endDate')

# %%
# parse historical timeseries to quant-core for estimation of parameters
r = HistoricalParametersCalcualtor.getHistoricalMeanReturns(
    historicalTimeSeries)
sigma = HistoricalParametersCalcualtor.getHistoricalVolatility(
    historicalTimeSeries)

# set paramters for price path simulations
# 1. to be set by end user
# 2. can be loaded as fixed parameters from a config file
tInYears = 1
numOfTradingDays = 252
numOfRuns = 1000

# Call quant-core methods to generate price paths
gbm = GBM(sInitial, r, sigma, tInYears, numOfRuns, numOfTradingDays)
pricepaths = gbm.generatePaths()
# print(pricepaths)


# %%
pathFrame = pd.DataFrame(pricepaths)
pathFrame.plot(legend=None)
print(pathFrame)

# %%
