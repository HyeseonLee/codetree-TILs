arr = list(map(int, input().split())) 

c_arr = [0 for _ in range(len(arr)+1)]
for elem in arr:
    if elem == 0:
        break
    c_arr[elem//10] += 1

for i in range(100,0,-10):
    print(f"{i} - {c_arr[i//10]}")