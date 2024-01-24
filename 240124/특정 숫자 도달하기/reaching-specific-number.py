arr = list(map(int, input().split()))
s=0
n_arr=[]
for item in arr:
    if item>=250:
        break  
    s+=item
    n_arr.append(item)

print(f"{s} {s/len(n_arr):.1f}")