c = 0
d=0
for i in range(10):
    a = int(input())
    if a>=0 and a<=200:
        c+=a
        d+=1

print(f"{c} {c/d:.1f}")