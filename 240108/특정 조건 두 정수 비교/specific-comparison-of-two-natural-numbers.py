a,b = map(int, input().split())

if a<b:
    print("1", sep=" ")
elif a>b:
    print("0", sep=" ")
elif a==b:
    print("1", sep=" ")
else:
    print("0", sep=" ")