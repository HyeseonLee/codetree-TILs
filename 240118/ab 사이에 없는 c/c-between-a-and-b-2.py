a,b,c = map(int, input().split())
state = True
for i in range(a,b+1):
    if i%7==0:
        state =False
if state==True:
    print("YES")
else:
    print("NO")