count = 0
result = []

while True:
    line = input()
    if line:
        if count == 0:
            count = 1
            continue
        x, n = [int(_) for _ in line.split()]
        r = 1
        if n == 0:
            result.append(r)
        else:
            for i in range(n):
                r = (r + x / r)/2
            result.append(r)
    else:
        break
print(*result)