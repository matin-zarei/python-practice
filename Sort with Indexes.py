line = input()
data = [int(_) for _ in line.split()]
legecy = data.copy()
change = True
while change:
    change = False
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            change = True
            data[i], data[i+1] = data[i+1], data[i]
for num in data:
    print(legecy.index(num)+1)

# u need to submit this first :)