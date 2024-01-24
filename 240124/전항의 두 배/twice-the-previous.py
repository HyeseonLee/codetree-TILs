a, b = map(int, input().split())

arr = [a,b]
# 3번째항부턴 = 전항 + *전전항*2)
for i in range(2,10):
    arr.append(arr[i-1]+(arr[i-2]*2))

for item in arr:
    print(item, end=" ")