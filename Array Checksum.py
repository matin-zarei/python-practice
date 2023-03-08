inputs = 0
result = 0
seed = 113
limit = 10000007
while True:
    line = input()
    if inputs == 0:
        inputs = line
        continue
    if line:
        data = [int(x) for x in line.split()]
        for item in data:
            result = (result + item) * seed
            if result > limit:
                result = result % limit
    else:
        break

print(result)
