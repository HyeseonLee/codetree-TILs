# print(최솟값, 최솟값을 갖는 원소 개수)
t_num = int(input())
arr = list(map(int, input().split()))

min_num = min(arr)
count = 0
for num in arr:
    if num==min_num:
        count += 1

print(min_num, count)