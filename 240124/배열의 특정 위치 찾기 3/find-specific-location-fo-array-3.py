arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    if arr[i] == 0:
        a=i
        break
print((arr[a-1]+arr[a-2]+arr[a-3]))