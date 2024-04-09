import sys
line = sys.stdin.readline().strip() # 개행문자가 포함되어있어서 제거해주기
stack = []

for i in range(len(line)):
    # ( 이면 stack에 넣어주기
    # ) 이면, stack에 (가 있는지 보고 -> 없으면 에러 / stack이 비어있어도 에러
    if line[i] == "(":
        stack.append(line[i])
    else:
        # ")"가 들어왔는데 stack이 비어있으면 wrong
        if len(stack)==0:
            print("No")
            break
        stack.pop()
    
    if len(stack)!=0:
        print("No")
        break
    print("Yes")