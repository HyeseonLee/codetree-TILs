# 내림차순으로 정렬했을 때, 첫번째랑 두번째 ? 에 쉽지 !

num = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
print(arr[0], arr[1])