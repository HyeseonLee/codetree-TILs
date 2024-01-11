year = int(input())
cnt = 0
for i in range(1,year+1):
    if (i%4==0 and i%100!=0) or i%400==0:
        #윤년
        cnt += 1

print(cnt)