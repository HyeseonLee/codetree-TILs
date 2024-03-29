a = int(input())

count = 1
# 9가 되었을 때, 다시 1로 초기화하도록 한다.

for i in range(0,a):
    for j in range (0,a):
        if count>=10:
            count = 1
        print(count, end=" ")
        count += 1
    print()