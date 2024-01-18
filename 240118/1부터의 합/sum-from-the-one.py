a = int(input())
s = 0
for i in range(100+1):
    s += i
    if s>=a:
        print(i)
        break