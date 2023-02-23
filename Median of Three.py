counter = 0
result = []
while True:
    data = input()
    if not data:
        break
    else:
        if counter == 0:
            counter += 1
            continue

        a, b, c = [int(x) for x in data.split()]
        if a > b:
            a,b = b,a
        if b > c:
            b,c = c,b
        if a > b:
            a,b = b,a

        result.append(b)

print(*result)


