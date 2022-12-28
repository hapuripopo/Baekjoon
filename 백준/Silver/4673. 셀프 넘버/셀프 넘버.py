def sequence(cstr):
    num = 0
    num += cstr
    while True:
        num += cstr % 10
        cstr = int(cstr/10)
        if cstr < 1:
            break

    return num


none_self_num = [sequence(i) for i in range(1, 10001)]
self_num = [i for i in range(1, 10001) if i not in none_self_num]

for i in self_num:
    print(i)
