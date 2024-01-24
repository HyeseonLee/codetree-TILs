n = int(input())

for i in range(n):
    for k in range(n-i+1):
        print(" ",end=" ")
    for j in range(2*n+1):
        print("*",end=" ")
    print()