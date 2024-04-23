import yfinance as yf

class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares
        self.data = yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]
    
    def update_price(self):
        self.data = yf.Ticker(self.symbol).history(period="1d")["Close"].iloc[-1]

class Portfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            print("Stock already exists in portfolio.")
        else:
            self.stocks[symbol] = Stock(symbol, shares)
    
    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
        else:
            print("Stock not found in portfolio.")
    
    def update_prices(self):
        for stock in self.stocks.values():
            stock.update_price()
    
    def total_value(self):
        total = 0
        for stock in self.stocks.values():
            total += stock.data * stock.shares
        return total

# Example usage:
portfolio = Portfolio()

# Adding stocks
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOGL", 5)
portfolio.add_stock("MSFT", 8)

# Removing a stock
portfolio.remove_stock("GOOGL")

# Updating prices
portfolio.update_prices()

# Printing total portfolio value
print("Total Portfolio Value: $", portfolio.total_value())
