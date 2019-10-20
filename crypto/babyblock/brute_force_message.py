from decrypt import generate_message

strs = ""
for i in range(1000):
    _sum = 2000 + i
    msg = generate_message(bytes(b"0ops{"), _sum)
    if i % 30 == 0:
        print("echo \"%s\" | nc 111.186.57.85 10080 > %d.txt" % (strs, _sum))
        strs = ""
    strs = strs + msg.hex() + "\\n"
