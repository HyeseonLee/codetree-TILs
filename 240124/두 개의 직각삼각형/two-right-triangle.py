n = int(input())

for i in range(n,0,-1):
    for _ in range(i):
        print("*",end="")
    for k in range(2*n-2*i):
        print(" ",end="")
    for _ in range(i):
        print("*",end="")
    print()