a, b = map(int, input())

big = a

while big>=b:
    if big%2==0:
        print(big, end=" ")
    big -= 1