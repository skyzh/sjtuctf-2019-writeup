from string import *

with open("output", "rb") as f:
    data = f.read()
    allow_char = digits + ascii_letters + punctuation + ' \n'
    stride = 29
    all_map = {}
    for j in range(0, stride):
        available_key = []
        for key in allow_char:
            flag = True
            for i in range(j, len(data), stride):
                if not(chr(data[i] ^ ord(key)) in allow_char):
                    flag = False
                    break
            if flag:
                available_key.append(key)
        print(available_key, " at %d" % j)
        all_map[j] = available_key