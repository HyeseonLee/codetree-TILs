a, b,c = map(int, input().split())
r = 'NO'
for i in range(1,b):
    if i%c==0:
        r = 'YES'
        break

print(r)