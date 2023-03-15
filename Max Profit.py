# what days should we buy and sell for max profit
stock_price = [6, 13, 2, 10, 3, 5]
max_profit = 0
min_stock_price = stock_price[0]
for price in stock_price:
    min_stock_price = min(price, min_stock_price)
    comparison_profit = price - min_stock_price
    max_profit = max(max_profit, comparison_profit)
print(max_profit)
