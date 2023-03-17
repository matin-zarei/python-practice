main_arr = [1, 2, 3, 4, 5]
alt_arr = [1, 2, 3, 5]

# for item in main_arr:
#     if item in alt_arr:
#         pass
#     else:
#         print(item)
#
# main_arr.sort()
# alt_arr.sort()
# alt_arr.append('dummy')
# for i in range(len(main_arr)):
#     if main_arr[i] != alt_arr[i]:
#         print(main_arr[i])
#         break

# sum1 = sum(main_arr)
# sum2 = sum(alt_arr)
# print(sum1 - sum2)

main_arr.sort()
alt_arr.sort()

for num1, num2 in zip(main_arr, alt_arr):
    if num1 != num2:
        print(num1)