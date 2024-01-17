# a의 b승은 어떻게 표현하지 ? a^3 = a * a* a

a, b = map(int, input().split())
prod = 1
for i in range(b):
    prod = prod*a

print(prod)