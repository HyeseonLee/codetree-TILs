a,b = map(int, input().split())

if a<b:
    print("1", end=" ")
elif a>b:
    print("0", end=" ")

if a==b:
    print("1", end=" ")
elif a!=b:
    print("0", end=" ")