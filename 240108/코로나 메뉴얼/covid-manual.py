a,b=input().split()
b=int(b)

c,d=input().split()
d=int(d)

e,f=input().split()
f=int(f)

num_A =0

if a=='Y':
    if b>=37:
        num_A += 1
if c=='Y':
    if d>=37:
        num_A += 1
if e=='Y':
    if f>=37:
        num_A += 1
if num_A>=2:
    print("E")
else:
    print("N")