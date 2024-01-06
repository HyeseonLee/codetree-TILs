list = list(map(int, input().split()))
print(sum(list))
print(sum(list)//len(list))
print(sum(list) - (sum(list)//len(list)))