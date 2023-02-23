data = []
while True:
    line = input()
    if line:
        if len(line.split()) < 2:
            continue
        a,b,c = [int(x) for x in line.split()]
        number = a*b+c
        digit = 0
        while number > 9:
            digit += number % 10
            number = number // 10
        digit += number
        data.append(digit)
    else:
        break

for i in data:
    print(i)