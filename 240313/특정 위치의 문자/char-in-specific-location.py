# you know , 갈팡 질팡하는 내 맘을 ,, 

char_arr = ['L', 'E', 'B', 'R', 'O', 'S']

a = input()

if a in char_arr:
    for i, value in enumerate(char_arr):
        if value==a:
            print(i)
if a not in char_arr:
    print('None')