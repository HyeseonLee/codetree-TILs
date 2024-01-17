# 만족하지 않는 수를 collecting할 때, continue 문으로 다시 for loop에 돌아가게 만들 수 있다.

a = int(input())

for i in range(1,a+1):
    if i%2==0 or i%10==5 or (i%3==0 and i%9!=0):
        continue
    print(i, end=" ")