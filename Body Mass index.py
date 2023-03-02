counter = 0
data = []
while True:
    line = input()
    if line:
        if counter == 0:
            counter = 1
            continue
        else:
            w,h = [float(x) for x in line.split()]
            bmi = w/(h**2)
            if bmi < 18.5:
                result = 'under'
            elif bmi < 25:
                result = 'normal'
            elif bmi < 30:
                result = 'over'
            else:
                result = 'obese'
            data.append(result)
    else:
        break

print(*data)