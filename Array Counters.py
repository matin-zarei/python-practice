counter = 0
results = {}
while True:
    line = input()
    if counter == 0:
        counter = 1
        alen = [int(x) for x in line.split()]
        intcount = alen[1] + 1
        for i in range(intcount):
            if i == 0:
                continue
            results[i] = 0
        continue
    if line:
        nums = [int(x) for x in line.split()]
        for num in nums:
            results[num] += 1
    else:
        break
print(*results.values())