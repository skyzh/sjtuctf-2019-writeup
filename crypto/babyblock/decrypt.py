msg = b'\xb6\xa7\xe1\x1bN\xd3\xe9k\x8d\xff\x1d\x12\\\x0eT\x93\xefy\xb0\xdd\x9a\xd8\x12\xf1\x03\xd6fk\x04\xcb'
msg_sum = 2740

def generate_message(_header, sum, length = 30):
    header = bytes(_header)
    for i in header:
        sum -= i
    while sum >= 0x100:
        header += bytes([0xff])
        sum -= 0xff
    header += bytes([sum])
    while len(header) < length:
        header += bytes([0])
    return header


header = bytes(b"0ops")
plain_text = bytes(header)
for j in range(30):
    plain = generate_message(header, msg_sum)
    assert(sum(bytes.fromhex(plain.hex())) == msg_sum)
    print(msg_sum)
    assert(len(plain) == len(msg))
    print(plain.hex())
    cipher = eval(input())
    i = len(header)
    new_x = bytes([cipher[i] ^ msg[i] ^ plain[i]])
    plain_text = plain_text + bytes([cipher[i] ^ msg[i] ^ plain[i]])
    header = bytes(plain_text)
    print(plain_text.decode(), new_x)