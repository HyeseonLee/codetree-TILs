n = int(input())
count = 0

for i in range(1,n+1):
    if n//i>1:
        print(n//i)
        n=n//i
        print(n)
        count += 1
    else:
        count+=1
        break

print(count)