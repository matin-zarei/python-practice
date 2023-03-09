counter = 0
a = 1
b = 1
while True:
    line = input()
    if counter == 0:
        counter = 1
        continue
    if line:
        x1, y1, x2, y2 = [int(x) for x in line.split()]
        #y1 = (a * x1) + b
        a = x1 // y1
        b = x1 % y1
        print(b)

    else:
        break
