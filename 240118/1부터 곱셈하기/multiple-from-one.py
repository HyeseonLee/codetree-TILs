n = int(input())
a = 1
for i in range(10+1):
    a *= i
    if a>=n:
        print(i)
        break