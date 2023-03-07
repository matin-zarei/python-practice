counter = 0
data = []
while True:
    line = input()
    if line:
        if counter == 0:
            counter = 1
            continue
        else:
            nums = [int(x) for x in line.split()]
            counter = summation = 0
            for item in nums:
                if item == 0:
                    break
                summation += item
                counter += 1
            result = summation/counter
            data.append(round(result))
    else:
        break

print(*data)