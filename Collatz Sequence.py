counter = 0
result = []

while True:
    line = input()
    if counter == 0:
        counter = 1
        continue
    if line:
        nums = [int(x) for x in line.split()]
        for num in nums:
            count = 0
            while num != 1:
                count += 1
                if num % 2 == 0:
                    num = int(num / 2)
                else:
                    num = int(3 * num + 1)
            result.append(count)
    else:
        break
print(*result)

