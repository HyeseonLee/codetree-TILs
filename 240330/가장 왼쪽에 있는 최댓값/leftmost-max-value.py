# 가장 왼쪽에 있는 최댓값?

# 최댓값의 위치를 출력
# 그 위치보다 앞에 있는 것들에서의 최댓값을 찾고, 그것의 위치를 출력

num = int(input())
arr = list(map(int, input().split()))


ind = num
while ind >1:
    for value in arr[:ind]:
        if value == max(arr[:ind]):
            print(arr.index(value)+1, end=" ")
            ind = arr.index(value)