import gmpy2
p = int(input())
a0 = int(input())
a1 = int(input())
a2 = int(input())
state = a2
m = (gmpy2.invert(a1 - a0, p) * (a2 - a1)) % p
c = (a1 - m * a0) % p

state = (m * state + c) % p
print(state)

state = (m * state + c) % p
print(state)

state = (m * state + c) % p
print(state)
