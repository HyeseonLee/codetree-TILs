a, b = map(int, input().split())

if a>=0:
    for _ in range(a):
        print(b, end="")
else:
    print("0")