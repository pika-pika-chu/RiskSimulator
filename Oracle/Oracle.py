import numpy as N


class Chainlink:

    def __init__(self):
        self.price = 1000
        self.histTimeSeries = N.array(
            [1000, 1010, 1025, 1100, 1085, 1035, 1056, 1075, 1024, 990, 925, 958, 935, 987, 1000])

    # dummy function to return price
    # eth price assumed to be $1000
    def getLatestPrice(self, ticker):
        return self.price

    # update price for a ticker
    def updatePrice(self, ticker, price):
        self.price = price

    # function to build out and return historical timeseries
    # from a start date to a given end date
    def getHistoricalPrices(self, ticker, startDate, endDate):
        return self.histTimeSeries
