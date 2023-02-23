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

        first, step, seq = [int(x) for x in data.split()]
        sequence_nums = [first]
        i = 1

        while i < seq:
            sequence_nums.append(next(reversed(sequence_nums)) + step)
            i += 1
        result.append(sum(sequence_nums))

print(*result)

# get last item of list using next(reversed(sequence_nums))
# using * to print all items of list
