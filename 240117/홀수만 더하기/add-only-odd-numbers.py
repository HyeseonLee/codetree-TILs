a = int(input())

c=0
for i in range(a):
    b = int(input())
    if b%2==1 and b%3==0:
        c+=b

print(c)