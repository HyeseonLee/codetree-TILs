a,b,c = map(int, input().split())


# 흠 중간값이라 !
if max(a,b,c)==c:
    if b>a:
        print(b)
    else:
        print(a)
if max(a,b,c)==a:
    if c>b:
        print(c)
    else:
        print(b)
if max(a,b,c)==b:
    if a>c:
        print(a)
    else:
        print(c)