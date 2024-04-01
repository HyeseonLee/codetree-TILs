# 가로 평균
# 세로 평균
# 전체 평균
n = 2
m = 4

outer = []

### 2차원 배열 만들기
for _ in range(n):
    outer.append(list(map(int, input().split())))

### 가로 평균
av_row = 0
av_col = 0
av_all = 0
for i in range(n):
    print(f'{sum(outer[i])/len(outer[i]):.1f}', end=" ")
print()

for i in range(m):
    sum_a = 0
    for j in range(n):
        sum_a += outer[j][i]
    print(f'{sum_a/2:.1f}', end=" ")
print()

s_all = 0
for i in range(n):
    for j in range(m):
        s_all += outer[i][j]
print(f'{s_all/n*m:.1f}')