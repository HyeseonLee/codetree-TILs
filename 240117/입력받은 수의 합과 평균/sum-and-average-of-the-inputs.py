s = 0
c = 0

a = int(input())

for i in range(a):
    b = int(input())
    s+=b
    c+=1

print(f"{s} {s/c:.1f}")