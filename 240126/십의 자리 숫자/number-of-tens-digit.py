arr = list(map(int, input().split())) 

c_arr = [0 for _ in range(10)]
for elem in arr:
    if elem == 0:
        break
    c_arr[elem//10] += 1

for i in range(1,10):
    print(f"{i} - {c_arr[i]}")