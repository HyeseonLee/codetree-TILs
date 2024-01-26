arr = list(map(int, input().split()))

c_arr = [0 for _ in range(7)]

for elem in arr:
    c_arr[elem] += 1

for i in range(1,7):
    print(f"{i} - {c_arr[i]}")