celsius = []

line = input()
counter = 0
if line:
    fahrenheit = [int(x) for x in line.split()]
    for i in fahrenheit:
        if counter == 0:
            counter += 1
            continue
        else:
            cel = (5/9)*(i - 32)
            celsius.append(round(cel))
            pass

for i in celsius:
    print(i)