sex = int(input())
age = int(input())

if age>=19:
    if sex==0:
        print("MAN")
    elif sex==1:
        print("WOMAN")
else:
    if sex==0:
        print("BOY")
    elif sex==1:
        print("GIRL")