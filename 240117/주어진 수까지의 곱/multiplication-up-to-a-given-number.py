a, b = map(int, input().split())
prod = 1

for i in range(a,b+1):
    prod = prod*i

print(prod)