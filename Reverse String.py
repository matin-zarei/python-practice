line = input()
result = []
data = line.split()


for item in data:
    str = item[::-1]
    result.append(str)
result.reverse()
print(*result)
