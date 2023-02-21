data = []
counter = 1

while True:
    line = input()
    if line:
        if counter == 1:
            counter += 1
            continue
        else:
            a, b = [int(x) for x in line.split()]

            data.append(min(a,b))
    else:
        break

for i in data:
    print(i)
