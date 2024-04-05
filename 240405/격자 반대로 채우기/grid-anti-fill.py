n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num =1
for i in range(n-1, -1, -1):
    if i%2 == 0:
        for j in range(n):
            arr[j][i] = num
            num += 1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] =num #[3][3] [2][3] [1][3] [0][3] / [0][2] [1][2] [2][2] [3][2]
            num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()