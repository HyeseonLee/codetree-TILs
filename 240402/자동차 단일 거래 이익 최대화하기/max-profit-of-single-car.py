num = int(input())
arr = list(map(int, input().split()))

# 자동차 한번 사서 되팔 때 이익이 최대화 되고자 한다. 
# 최대 이익을 출력
# 이익이 나지 않는 경우 0 출력

# n 년간의 가격 정보가 주어진다.
# 모든 쌍에 대하여 비교를 해야한다. 
plus_arr = []

for index, price in enumerate(arr):
    for comp in arr[index+1:]:
        if comp<=price:
            pass
        else:
            plus_arr.append(comp-price)

if plus_arr:
    print(max(plus_arr))
else:
    print("0")