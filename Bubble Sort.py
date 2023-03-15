input = input()
swaps, passes, temp = 0, 0, 0
data = [int(_) for _ in input.split()]
while True:
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            swaps += 1
    passes += 1
    if temp == swaps:
        break
    temp = swaps
print(passes, swaps)
print(*data)




