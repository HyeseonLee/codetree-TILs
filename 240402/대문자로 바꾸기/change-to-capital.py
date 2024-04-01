n = 5
m = 3

for _ in range(n):
    arr = list(input().split())
    for i in range(m):
        print(arr[i].upper(),end=" ")
    print()