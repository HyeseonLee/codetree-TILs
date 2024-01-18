n = int(input())
state='P'
for i in range(2,n):
    if n%i==0:
        state = 'C'

print(state)