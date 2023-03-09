# Write a function:that, given an array A of N integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying,
# publication or disclosure prohibited.
A = [1, 3, 6, 4, 1, 2]
A = [1, 2, 3]
A = [0, 0]
smallest = 0
A.sort()
for num in A:
    if num < 1:
        continue
    elif (num - smallest) <= 1:
        smallest = num
    else:
        break
print(smallest+1)


