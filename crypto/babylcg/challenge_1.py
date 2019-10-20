import gmpy2
p = int(input())
m = int(input())
state = int(input())
b = int(input())
c = (b - m * state) % p

state = (m * state + c) % p

state = (m * state + c) % p
print(state)

state = (m * state + c) % p
print(state)

state = (m * state + c) % p
print(state)