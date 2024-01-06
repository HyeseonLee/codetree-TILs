height, weight = map(int, input().split())

bmi = weight // ((height/100)**2)

print(int(bmi))
if bmi>=25:
    print("Obesity")