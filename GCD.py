result =''
while True:
    line = input()
    if line:
        f = [int(_) for _ in line.split()]
        a, b = f[0], f[1]
        while f[0] != f[1]:
            f.sort()
            f[1] = f[1] - f[0]
        gcd = f[1]
        lcm = int(a * b / gcd)
        result += '('+str(gcd)+' '+str(lcm)+') '
    else:
        break
print(result)
# old wile loop:
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# return a

# using recurcive
# function def gcd(a, b):
#     if a != b:
#         if max(a, b) % min(a, b) == 0:
#             return min(a,b)
#         return gcd(max(a, b) % min(a, b), min(a, b))
#     else:
#         return a