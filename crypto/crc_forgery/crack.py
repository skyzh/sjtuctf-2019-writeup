#!/usr/bin/env python3
# coding=utf-8

import binascii
import os
import random


def b2n(b):
    res = 0
    for i in b:
        res *= 2
        res += i
    return res


def n2b(n, length):
    tmp = bin(n)[2:]
    tmp = '0'*(length-len(tmp)) + tmp
    return [int(i) for i in tmp]


def s2n(s):
    return int(binascii.hexlify(s), 16)


def crc64(msg):
    msg = n2b(s2n(msg), len(msg)*8)
    msg += const
    for shift in range(len(msg)-64):
        if msg[shift]:
            for i in range(65):
                msg[shift+i] ^= poly[i]
    res = msg[-64:]
    return b2n(res)


const = n2b(0xdeadbeeffeedcafe, 64)
poly = n2b(0x10000000247f43cb7, 65)

msg_str = input()
blank_begin = msg_str.find("_") * 4
blank_end = blank_begin + 64
msg = bytes.fromhex(msg_str.replace("_", "0"))

crc = n2b(0x1337733173311337, 64)

plain_msg = n2b(s2n(msg), len(msg)*8) + const
crc_msg = [0] * (len(msg) * 8) + crc

print("cracking %d - %d bit" % (blank_begin, blank_end))
for shift in range(2047, blank_begin - 1, -1):
    if plain_msg[shift + 64] != crc_msg[shift + 64]:
        for i in range(65):
            crc_msg[shift + i] ^= poly[i]
    assert(crc_msg[shift + 64] == plain_msg[shift + 64])

for shift in range(0, blank_begin):
    if plain_msg[shift]:
        for i in range(65):
            plain_msg[shift+i] ^= poly[i]

blank = [0] * 64
print(plain_msg[blank_begin:blank_end])
print(crc_msg[blank_begin:blank_end])
for i in range(blank_begin, blank_end):
    blank[i - blank_begin] = plain_msg[i] ^ crc_msg[i]
print(blank)
print(hex(b2n(blank))[2:])
