arr = list(map(int, input().split())) 

# 10점부터 100점까지 10개 필요 ! 1 ~ 10 까지 필요 !
c_arr = [0 for _ in range(11)]

for elem in arr:
    if elem == 0:
        break
    c_arr[elem//10] += 1

for i in range(10,0,-1):
    print(f"{i*10} - {c_arr[i]}")