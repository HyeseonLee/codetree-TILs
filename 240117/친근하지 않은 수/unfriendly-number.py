# 2, 3, 5로 나누어지는 수

a = int(input())
c = 0
for i in range(1,a+1):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    c+=1


print(c)