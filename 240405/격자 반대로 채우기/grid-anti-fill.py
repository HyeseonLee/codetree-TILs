n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num =1
for i in range(n-1, -1, -1):
    # n이 4이면 3이 마지막열 
    # n이 5이며 4가 마지막역
    if n%2 != i%2:
        for j in range(n-1, -1, -1):
            arr[j][i] =num #[3][3] [2][3] [1][3] [0][3] / [0][2] [1][2] [2][2] [3][2]
            num += 1

    else:
        for j in range(n):
            arr[j][i] = num
            num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()