num = int(input())
arr=[]


for i in range(num):
    a = input()
    if " " in a:
        a,b = a.split()
        if a=="push_back":
            arr.append(b)
        elif a=="get":
            print(arr[int(b)-1])
    if a=="size":
        print(len(arr))
    if a=="pop_back":
        arr.pop()