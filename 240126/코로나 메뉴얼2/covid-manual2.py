# 코로 ~ 나 메뉴 ~ 얼


l = [0,0,0,0]

for _ in range(3):
    e = 0
    s,t = input().split()

    if s=='Y' and int(t)>=37:
        l[0]+=1
    elif s=='Y' and int(t)<37:
        l[2] += 1
    elif s=='N' and int(t)>=37:
        l[1] += 1
    elif s=='N' and int(t)<37:
        l[3] += 1

for elem in l:
    print(elem, end=" ")

if l[0]>=2:
    print('E')