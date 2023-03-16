letters = 'AABBCCCa'
run = ''
i = 1
cnt = 1
while i < len(letters):
    if letters[i] == letters[i-1]:
        cnt += 1
    else:
        run = run+letters[i-1]+str(cnt)
        cnt = 1
    i += 1

print(run)






# letters = 'AABBCCCa'
# dic = {}
# for letter in letters:
#     if letter in dic:
#         dic[letter] += 1
#     else:
#         dic[letter] = 1
#
# result = ''
# for key,value in dic.items():
#     result = result+str(key)+str(value)
# print(result)

