arr = list(map(int, input().split()))

for index, num in enumerate(arr):
    if num==999 or num==-999:
        print(max(arr[:index]),min(arr[:index]))