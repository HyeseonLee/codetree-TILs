arr = list(map(int, input().split()))
odd = sum(arr[::2])
even = sum(arr[1::2])

if odd >= even:
    print(odd-even)
else:
    print(even-odd)