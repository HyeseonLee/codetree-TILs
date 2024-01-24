n = int(input())
arr=[1,n]
p=1
while True:
    p+=1
    arr.append(arr[p-1]+arr[p-2])
    # 존재하지 않는 arr 인덱스 조회시 당연히 오류가 나지 바보야 !
    if arr[p] > 100:
        break
    
for i in arr:
    print(i, end=" ")