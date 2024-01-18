# 소수 : 약수가 1과 자기 자신뿐인 수
n = int(input())
s = 'N'
for i in range(2,n):
    if n%i == 0 :
        s='C'
    
print(s)