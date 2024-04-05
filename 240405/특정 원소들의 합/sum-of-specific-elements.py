outer= []
for _ in range(4):
    arr = list(map(int, input().split()))
    outer.append(arr)

res = 0
# 1, 1,2, 1,2,3, 1,2,3,4
for i in range(4):
    for j in range(i+1):
        res += outer[i][j]
        
print(res)