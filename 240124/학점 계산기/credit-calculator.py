n = int(input())
arr = list(map(float, input().split()))

sc = sum(arr)/n
sc2 = ""
if sc>=4.0:
    sc2 = "Perfect"
elif sc>=3.0:
    sc2="Good"
else:
    sc2="Poor"
print(f"{sc:.1f}")
print(sc2)