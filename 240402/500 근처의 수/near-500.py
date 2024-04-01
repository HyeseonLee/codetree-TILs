arr = list(map(int, input().split()))

# 500 미만의 수 중 가장 큰 수
# 500 초과 중 가장 작은 수
min_arr =[]
max_arr = []

for i in range arr:
    if i<500:
        min_arr.append(i)  
    if i>500:
        max_arr.append(i)

print(max(min_arr), min(max_arr))