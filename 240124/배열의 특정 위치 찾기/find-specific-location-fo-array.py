arr = list(map(int, input().split()))

print(sum(arr[1::2]),end=" ")
print(f"{sum(arr[2::3])/len(arr[2::3]):.1f}")