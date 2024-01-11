a, b = map(int, input().split())

print(a//b, end=".")

rest = a%b
for _ in range(20):
    print((rest*10) // b, end="")
    rest = rest*10 % b