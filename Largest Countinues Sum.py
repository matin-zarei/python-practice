data = [2, 3, -10, 9, 2]
total_sum = 0
for i in range(len(data)):
    local_sum = 0
    for j in range(i, len(data)):
        temp_sum = local_sum + data[j]
        if temp_sum > local_sum:
            local_sum = temp_sum
            total_sum = max(total_sum, local_sum)
        else:
            total_sum = max(total_sum, local_sum)
            break
print(total_sum)
