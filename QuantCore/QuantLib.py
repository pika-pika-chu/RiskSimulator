import numpy as np


class GBM:

    # Class for price path simulations

    def __init__(self, sInitial, r, sigma, tInYears, numOfRuns, numOfTradingDays):
        self.sInitial = sInitial
        self.r = r
        self.sigma = sigma
        self.tInYears = tInYears
        self.numOfRuns = numOfRuns
        self.numOfTradingDays = numOfTradingDays

    def generatePaths(self):
        dt = float(self.tInYears) / self.numOfTradingDays
        paths = np.zeros((self.numOfTradingDays + 1,
                         self.numOfRuns), np.float64)
        paths[0] = self.sInitial
        for t in range(1, self.numOfTradingDays + 1):
            rand = np.random.standard_normal(self.numOfRuns)
            paths[t] = paths[t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * dt +
                                             self.sigma * np.sqrt(dt) * rand)
        return paths


class HistoricalParametersCalcualtor:
    # dummy function to return historical mean of a timeseries
    def getHistoricalMeanReturns(historicalTimeSeries):
        return 0.05

    def getHistoricalVolatility(historicalTimeSeries):
        return 0.20


class VaRCalculator:

    def calculateVar():
        pass
