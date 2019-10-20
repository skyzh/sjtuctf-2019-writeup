from string import *

mapping = "pxsezahfytirowdjcmgnulkvbq"
d = dict(zip(mapping, ascii_lowercase))
d.update({k.upper(): v.upper() for k, v in d.items()})
mapping = str.maketrans(d)
print(mapping)
with open("output", "rb") as f:
    with open("dec", "w") as out:
        data = f.read()
        #         ?      ?              ? ??
        #      01234567890123456789012345678
        key = "secret_xor_key_for_u_to_crack"
        i = 0
        for ch in data:
            if key[i] != '-':
                c = ord(key[i]) ^ ch
                if c in mapping:
                    out.write(mapping[ord(key[i]) ^ ch])
                else:
                    out.write(chr(c))
            else:
                out.write(b'?')
            i = (i + 1) % len(key)
