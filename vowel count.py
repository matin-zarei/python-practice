data = []
counter = 1
vowels = [x for x in 'aouiey']
while True:
    line = input()
    if line:
        if counter == 1:
            counter += 1
            continue
        else:
            count = 0
            for i in line:
                if i in vowels:
                    count += 1
            data.append(count)


    else:
        break

for i in data:
    print(i)