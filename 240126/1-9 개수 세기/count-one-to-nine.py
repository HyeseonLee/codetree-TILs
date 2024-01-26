n = int(input())
arr = list(map(int, input().split()))

c_arr = []
for i in range(10):
    c_arr.append(0)

for elem in arr:
    c_arr[elem] += 1

for elem in c_arr[1:]:
    print(elem)