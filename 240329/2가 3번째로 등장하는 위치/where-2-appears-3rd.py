num = int(input())
arr = list(input().split())
count = 0
# 3번째로 등장할 때, 해당 index를 출력하는 것이다.
for index, value in enumerate(arr):

    if value == '2':
        count += 1
    if count==3:
        print(index+1)
        break