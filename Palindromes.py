import re
result = []
first_line = True
while True:
    line = input()
    if line:
        if first_line:
            first_line = False
            continue
        else:
            regex = re.compile('[^a-zA-Z]')
            trimmed = regex.sub('', line)
            trimmed = trimmed.lower()
            answer = 'Y'
            t_lenth = len(trimmed) // 2
            for i in range(t_lenth):
                if trimmed[i] != trimmed[-(i+1)]:
                    answer = 'N'
            result.append(answer)
    else:
        break
print(*result)
# the better way is to compare the string with its reverse
# if ns == ns[::-1]:
#     return 'Y'
# else:
#     return 'N'
