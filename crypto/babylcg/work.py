
from hashlib import sha256
import string
import random
import codecs

chal = "5ecd5b9fb089dfdc".decode("hex")

def randomString(stringLength=16):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
i = 0

while True:
    sol = randomString()
    i = i + 1
    if i % 100000 == 0:
        print(i, sol)
    if sha256(chal + sol).digest().startswith('\xdd\xdd\xdd'):
        print(sol)
        break
