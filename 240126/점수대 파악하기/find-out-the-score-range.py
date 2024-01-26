arr = list(map(int, input().split())) 

c_arr = [0 for _ in range(len(arr)+1)]
for elem in arr:
    if elem == 0:
        break
    c_arr[elem//10] += 1

for i in range(len(arr),0,-1):
    print(f"{i*10} - {c_arr[i]}")