counter = 0
result = []
while True:
    line = input()
    if counter == 0:
        counter = 1
        continue
    if line:
        sd, sh, sm, ss, ed, eh, em, es = [int(x) for x in line.split()]
        total_start = (((sd * 24 + sh) * 60 + sm) * 60) + ss
        total_end   = (((ed * 24 + eh) * 60 + em) * 60) + es
        def_time = total_end - total_start
        fd = def_time // 86400
        def_time = def_time % 86400
        fh = def_time // 3600
        def_time = def_time % 3600
        fm = def_time // 60
        def_time = def_time % 60
        fs = def_time
        data = '('+str(fd)+' '+str(fh)+' '+str(fm)+' '+str(fs)+')'
        result.append(data)

    else:
        break

print(*result)
