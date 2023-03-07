counter = 0
data = []
while True:
    line = input()
    if line:
        if counter == 0:
            counter = 1
            continue
        else:
            nums = [x for x in line.split()]
            for item in nums:
                counter, summation = 1, 0
                for num in item:
                    summation += int(num) * counter
                    counter += 1
                data.append(summation)
    else:
        break

print(*data)