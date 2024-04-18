def p(n):
    if n==0:
        return
    p(n-1)
    print(n, end=" ")
def p2(n):
    if n==0:
        return
    print(n, end=" ")
    p2(n-1)   
p(7)
print()
p2(7)