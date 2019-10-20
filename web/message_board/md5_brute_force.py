from hashlib import md5
import string
import random


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


i = 0
while True:
    s = randomString()
    d = md5(s).hexdigest()
    i = i + 1
    if i % 10000 == 0:
        print i
    if d[0:6] == "efc4a9":
        print s
        break
