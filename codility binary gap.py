def solution(N):
    data = bin(N)
    print(data)
    gap = 0
    counter = 0
    first_item = True
    for item in data:
        if item == '0':
            if first_item:
                first_item = False
                continue
            counter += 1
        else:
            if counter > gap:
                gap = counter
                counter = 0
                first_item = True
    return gap

print(solution (328))