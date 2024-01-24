n = int(input())

# 1부터 n까지 (n번 출력)
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print("",end="\n\n")

# n-1부터 1까지 출력
for i in range(n-1, 0,-1):
    for j in range(i):
        print("*", end="")
    print("", end="\n\n")