# 최댓값을 구하는 로직 
# 우엥  배가 고픈데 집에서 뭘 해먹기가 싫은데 배는 고파 
# 초기값을 설정하고 
# 배열을 돌면서 그것보다 크다면, 변수를 갱신하기

# 초기값을 어떻게 설정하지?
# 1. 첫번째 원소로 하기

# max_val = arr[0]
# for elem in arr[1:]:
#     if elem>max_val:
#         max_val = elem

arrr = list(map(int,input().split()))

print(max(arrr))