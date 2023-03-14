result, count = 0, 0
seed = 113
limit = 10000007

while True:
    line = input()
    if line:
        data = [int(_) for _ in line.split()]
        data.pop()
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                count += 1
        for item in data:
            result = (result + item) * seed
            if result > limit:
                result = result % limit
    else:
        break


print(count, result)


