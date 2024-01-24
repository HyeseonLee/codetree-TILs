n = int(input())
cnt = 0
a = 1
n_arr=[]
while cnt<2:
    n_arr.append(n*a)

    if (n*a) %5==0:
        cnt+=1

    a+=1

for item in n_arr:
    print(item, end=" ")