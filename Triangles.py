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
        answer = 1
        if a+b < c or a+c < b or b+c < a:
            answer = 0
        result.append(answer)

print(*result)


