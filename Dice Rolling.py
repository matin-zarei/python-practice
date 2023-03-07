counter = 0
result =[]
while True:
    line = input()
    if counter == 0:
        counter =1
        continue
    if line:
        data = float(line) * 6
        data = int(data)
        data += 1
        result.append(data)
    else:
        break

print(*result)