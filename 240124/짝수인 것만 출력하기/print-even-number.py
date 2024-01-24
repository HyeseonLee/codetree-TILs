n = int(input())
arr = list(map(int, input().split()))
n_arr = []
for i in range(n):
    if arr[i]%2==0:
        n_arr.append(arr[i])
    
for item in n_arr:
    print(item, end=" ")