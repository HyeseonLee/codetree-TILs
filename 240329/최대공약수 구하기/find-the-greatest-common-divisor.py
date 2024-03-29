# 최대 공약수를 어떻게 구하지 ? 
# 둘로 다 나누어떨어지는 수 ! 중 제일 큰 수 ! 
# 제일 큰 수를 어떻게 찾지 ?? 숫자 둘 중 더 큰 수 잡아서 그것보다 1개씩 작은 숫자로 테스트해볼까?

num1, num2 = map(int, input().split())
test_num = max(num1, num2)

for i in range(test_num,0,-1):
    if num1%i==0 and num2%i==0:
        print(i)
        break