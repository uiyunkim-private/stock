import yfinance as yf
import matplotlib
#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

print(tickerDf['Open'])

matplotlib.pyplot(tickerDf['Open'])
matplotlib.pyplot.show()