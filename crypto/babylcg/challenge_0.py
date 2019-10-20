import gmpy2
p = int(input())
m = int(input())
c = int(input())
state = int(input())
state = (m * state + c) % p
print(state)
state = (m * state + c) % p
print(state)
state = (m * state + c) % p
print(state)

