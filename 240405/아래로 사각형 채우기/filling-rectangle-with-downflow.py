n = int(input())
num = 1
for i in range(n):
    num = i+1
    for j in range(n):
        print(num, end=" ")
        num += n
    print()