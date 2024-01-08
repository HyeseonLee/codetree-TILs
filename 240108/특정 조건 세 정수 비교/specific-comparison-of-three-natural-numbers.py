a, b, c = map(int, input().split())

mi = min(a,b,c)

print("1", end=" ") if a==mi else print("0", end=" ")
print("1", end=" ") if a==b and b==c else print("0", end=" ")