a,b = map(int,input().split())

arr = [a,b,0,0,0,0,0,0,0,0]

for i in range(2,10):
    arr[i] = (arr[i-1] + arr[i-2])%10

for item in arr:
    print(item,end=" ")