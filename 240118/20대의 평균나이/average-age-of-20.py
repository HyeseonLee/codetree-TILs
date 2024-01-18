# 특정 조건이 될 때까지 쭉 받기
s = 0
c = 0
while True:
    age=int(input())
    if age>29 or age<20:
        break
    else:
        s += age
        c+=1

print(f"{s/c:.2f}")