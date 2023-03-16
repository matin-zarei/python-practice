# what days should we buy and sell for max profit
data = [6, 13, 2, 10, 3, 5]
result={}
b_date, s_date, profit = 0, 0, 0
for i in range(len(data)):
    for j in range (i, len(data)):
        if data[j] - data[i] > profit:
            profit = data[j] - data[i]
            b_date, s_date = data[i], data[j]
print()
