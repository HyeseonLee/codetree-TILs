a,b,c = map(int, input().split())
state = False
for i in range(a,b+1):
    if i%7==0:
        state =True
if state==True:
    print("YES")
else:
    print("NO")