n = 3

arr1=[]
arr2=[]

for i in range(n):
    row = list(map(int, input().split()))
    arr1.append(row)

blank = input()

for i in range(n):
    row = list(map(int, input().split()))
    arr2.append(row)


for i in range(n):
    for j in range(n):
        print(arr1[i][j]*arr2[i][j], end=" ")
    print()