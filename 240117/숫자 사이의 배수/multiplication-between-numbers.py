a,b = map(int, input().split())
c=0
d=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        c+=i
        d+=1

if d!=0:
    print(f"{c} {c/d:.1f}")
else:
    print(f"{c} {c/1:.1f}")