num = int(input())
arr = list(map(int, input().split()))

# 오름차순으로 옵니다.
# 서로 다른 두 숫자 고를 때, 차가 최소가 되는경우의 차는 ?

    # 차이가 최소가 되어야해.
    # 엥 그러면 min_thing을 어떻게 판단하지 ? 음 .. 아마 .. 오름차순이니까 앞 뒤를 비교하면 되지 않을까?
min_difference = arr[1]-arr[0]
for i in range(num):
    if i==0:
        difference1 = arr[i+1] - arr[i]
        difference2 = arr[i+1] - arr[i]
    elif i==num-1:
        difference1 = arr[i]-arr[i-1]
        difference2 = arr[i]-arr[i-1]

    else:        
        difference1 = arr[i]-arr[i-1]
        difference2 = arr[i+1] - arr[i]

    #print(difference1,difference2)    

    if min_difference>difference1:
        min_difference = difference1
    elif min_difference>difference2:
        min_difference = difference2
    #print("min", min_difference)
print(min_difference)