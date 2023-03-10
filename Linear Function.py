counter, a, b = 0, 1, 1
result = []
while True:
    line = input()
    if counter == 0:
        counter = 1
        continue
    if line:
        x1, y1, x2, y2 = [int(x) for x in line.split()]
        a = int((y2 - y1) / (x2 - x1))
        b = -a * x1 + y1
        data = '('+str(a)+' '+str(b)+')'
        result.append(data)

    else:
        break

print(*result)
