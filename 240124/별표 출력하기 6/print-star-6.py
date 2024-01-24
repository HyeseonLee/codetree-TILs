n = int(input())

for i in range(n,0,-1):
    for h in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

for i in range(n-2, -1, -1):
    # if n=3, i = 1, 2
    for h in range(i):
        print(" " , end=" ")
    for k in range((2*n)-(2*i)-1):
        print("*", end=" ")
    print()