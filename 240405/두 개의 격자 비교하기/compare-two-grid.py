n,m = map(int, input().split())

# 두개의 격자 만들기
arr1 = []
arr2 = []

for i in range(n*2):
    row = list(map(int, input().split()))
    if i<4:
        arr1.append(row)
    else:
        arr2.append(row)


# 같은 위치에 존재ㅎ는 숫자 값 같으면 0, 다르면 1
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print("0", end=" ") 
        else:
            print("1", end=" ")
    print()