# 중복하여 등장하지 않는 숫자 중 최댓값?
# 중복값 제거 어떻게 했더라?

# 다 중복이 된다면?

num = int(input())
arr = list(map(int, input().split()))
target_arr = []

for i in arr:
    # 중복하지 않는 것
    if i not in target_arr:
        target_arr.append(i)

if target_arr == []:
    print("-1")
else:
    print(max(target_arr))