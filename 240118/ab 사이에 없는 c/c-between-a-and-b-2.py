a,b,c = map(int, input().split())
state = True
for i in range(a,b+1):
    if i%c==0:
        state =False
if state==True:
    print("YES")
else:
    print("NO")