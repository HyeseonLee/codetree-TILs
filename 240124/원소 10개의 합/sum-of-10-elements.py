arr = list(map(int, input().split()))
# 아직은 list랑 map 자료형이 뭐가 다른지 모르겠다. 

s = 0
for i in arr:
    s += i
print(s)