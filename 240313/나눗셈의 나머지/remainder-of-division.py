# a를 b로 나눈 몫을 또 a로 나눈다. (a가 1 이하가 되기 전까지)
# 나머지가 나온 횟수를 저장한다.
# 나머지가 나온 횟수들의 제곱을 더해 출력한다.


a,b = map(int, input().split())
c=0
res=0
nam_arr=[0 for _ in range(11)]

while(a>1):
    c = a%b
    a = a//b
    nam_arr[c] += 1

for item in nam_arr:
    res += (item**2)

print(res)