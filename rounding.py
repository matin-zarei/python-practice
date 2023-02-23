import math


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
            frac, whole = math.modf(a / b)
            if frac != 0.5:
                data.append(round(a/b))
            elif a < 0 or b < 0:
                data.append(round(a/b) - 1)
            else:
                data.append(round(a/b))

    else:
        break

for i in data:
    print(i)

# frac, whole = math.modf(a / b)
# print(whole,frac)
# print ((a//b))
# if frac != 0.5:
#     data.append((a // b) + 1)
# elif a < 0 or b < 0:
#     data.append((a // b) - 1)
# else:
#     data.append((a // b) + 1)