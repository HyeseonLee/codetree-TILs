n = int(input())
arr = [
    input()
    for _ in range(n)
]

sum_ = 0
cnt = 0
# 모든 문자열 길이 합
for elem in arr:
    sum_ += len(elem)
    if elem[0] == "a":
        cnt += 1
print(sum_, cnt)