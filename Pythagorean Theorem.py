first_line = True
result = []
while True:
    line = input()
    if line:
        if first_line:
            first_line = False
            continue
        else:
            a, b, c = [int(_) for _ in line.split()]
            x = a**2 + b**2
            if x == c**2:
                answer = 'R'
            elif x < c**2:
                answer = 'O'
            else:
                answer = 'A'
            result.append(answer)
    else:
        break
print(*result)
