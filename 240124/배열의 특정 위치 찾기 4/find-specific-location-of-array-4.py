arr = list(map(int, input().split()))
cnt_2=0
s=0
for item in arr:
    if item==0:
        break
    if item%2==0:
        cnt_2+=1
        s += item
    
print(cnt_2, s)