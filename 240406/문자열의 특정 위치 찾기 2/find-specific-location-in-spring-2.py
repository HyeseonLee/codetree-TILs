# 최화
a = ["apple", "banana", "grape", "blueberry", "orange"]
b = input()
cnt = 0
for elem in a:
    if b == elem[2]:
        print(elem)
        cnt+=1
    if b == elem[3]:
        print(elem)
        cnt+=1
print(cnt)