n = int(input())

# n개부터 1개까지 출력하고 (n)

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# 1+1개부터 n개까지 출력
for i in range(2,n+1,+1):
    for j in range(i):
        print("*", end=" ")
    print()