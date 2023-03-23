result = []

while True:
    line = input()
    if line:
        char_num, string = line.split()
        char_num = int(char_num)
        if char_num > 0:
            chars = string[:char_num]
            new_string = string[char_num:]
            new_string = new_string + chars
            result.append(new_string)
        else:
            chars = string[char_num:]
            new_string = string[:char_num]
            new_string = chars + new_string
            result.append(new_string)
    else:
        break
print(*result)
