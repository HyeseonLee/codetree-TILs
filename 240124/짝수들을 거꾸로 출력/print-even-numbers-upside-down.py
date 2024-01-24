n = int(input())
arr = list(map(int, input().split()))
n_arr=[]
for item in arr:
    if item %2==0:
        n_arr.append(item)

for i in range(len(n_arr)-1, -1, -1):
    print(n_arr[i],end=" ")