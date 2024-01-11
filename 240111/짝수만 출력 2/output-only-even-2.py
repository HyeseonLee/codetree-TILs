a, b = map(int, input().split())

big = a

while big>=b:
    if big%2==0:
        print(big, end=" ")
    big -= 1