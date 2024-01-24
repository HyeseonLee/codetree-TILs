n = int(input())
arr = list(map(int, input().split()))

n_arr = [i**2 for i in arr]

for item in n_arr:
    print(item,end=" ")