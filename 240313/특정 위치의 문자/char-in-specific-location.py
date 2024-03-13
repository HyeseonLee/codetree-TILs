# you know , 갈팡 질팡하는 내 맘을 ,, 

char_arr = ['L', 'E', 'B', 'R', 'O', 'S']

a = input()

if a not in char_arr:
    print('None')
else:
    # char_arr에 a가 있다는 가정이 성립했으니까
    # index 위치를 알면 되네

    # index 위치를 알아내는 방법 1
    # for i, value in enumerate(char_arr):
    #     if value==a:
    #         print(i)  
    print(char_arr.index(a))