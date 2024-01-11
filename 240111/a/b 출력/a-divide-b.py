a, b = map(int, input().split())

print(a//b, end=".")

rest = a

for _ in range(20):
    if a//b > 0:
        print((rest-b)*10 // b, end="")
        rest = (rest-b)*10 % b

    else:
        print((rest*10) // b, end="")
        rest = rest*10 % b