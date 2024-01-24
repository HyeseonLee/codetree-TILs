arr = list(map(int, input().split()))
n_arr=[]
for a in arr:
    if a == 0:
        break
    n_arr.append(a)


for i in range(len(n_arr)-1,-1, -1):
    print(n_arr[i],end=" ")