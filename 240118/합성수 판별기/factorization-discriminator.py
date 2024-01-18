# 소수 : 약수가 1과 자기 자신뿐인 수
n = int(input())
s = ''
for i in range(2,n):
    if n%i != 0 :
        #나누어떨어지지않아
        s='C'
    else:
        s='N'
print(s)