a,b = map(int, input().split())
state = 0
for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        state = 1
    
print(state)