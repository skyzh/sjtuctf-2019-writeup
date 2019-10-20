a = ['c']
b = ['m', 'n', 'p', 'q', 'r', 's', 'v', 'y', '{', '|']
c  = ['a']
d = ['a', 'b', 'c', 'g', 'h', 'j', 'm', "'", '`', '|']
e = ['b', 'e', 'h', 'i', 'j', 'k', 'o', 't', 'w', '`']

for _a in a:
    for _b in b:
        for _c in c:
            for _d in d:
                for _e in e:
                    print(_a+_b+_c+_d+_e)