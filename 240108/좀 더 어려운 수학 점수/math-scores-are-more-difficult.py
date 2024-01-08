# 영어 < 수학

# 수학이 높으면 출력
# 수학 같으면 -> 영어 비교

#수학 영어
a,b = map(int, input().split())
c,d = map(int, input().split())

if a>c:
    print("A")
elif a<c:
    print("B")
elif a==c:
    if b>d:
        print("A")
    else:
        print("B")