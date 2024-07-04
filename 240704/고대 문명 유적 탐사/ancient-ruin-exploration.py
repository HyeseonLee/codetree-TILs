import sys
from copy import deepcopy
from collections import deque

#     
def make_boxes(table):
    boxes = []
    for i in range(3):
        for j in range(3):
            # 3by3 테이블 만들었다.
            box = [row[j:j+3] for row in table[i:i+3]]
            # 90, 180, 270 돌린 버전들을 만들어서 boxes에 넣자.
            origin_table = deepcopy(table)
            for degree in [90,180,270]:
                rotated_box = turn(degree,box)
                for m in range(3):
                    for n in range(3):
                        origin_table[i+m][j+n] = rotated_box[m][n]
                boxes.append({"table":deepcopy(origin_table),"center":(i+1, j+1), "degree":degree, "value":0}) # box 데이터, 중심 좌표(y,x)

                box = rotated_box
    return boxes

          
def turn(degree, table):
    count = degree//90
    new = [[0]*3 for _ in range(3)]

    for _ in range(count):
        for i in range(3):
            for j in range(3):
                new[i][j] = table[2-j][i]
    return new

def find_first_gotten_value(table):
    total_value = 0

    # 테이블의 모든 곳에 대하여 dfs를 진행해야 한다.
    visited = [[False]*5 for _ in range(5)]

    def dfs(y,x, table,visited):
        # 1. 체크인
        visited[y][x] = True
        count = 1
        # 2. 종료 조건인가? : 얘는 사실상 끝까지 돌아야하기 때문에 종료 조건이 무의미

        # 3. 연결된 곳 순회 : 상하좌우
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):
            newy = y+dy[i]
            newx = x+dx[i]

            # 4. 갈 수 있나?
            if 0<=newx<=4 and 0<=newy<=4:
                if not visited[newy][newx] and table[y][x] == table[newy][newx]:
                    # 5. 가자
                    visited[newy][newx] = True
                    count += dfs(newy, newx, table, visited)

        # 6. 체크아웃
        return count

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                count = dfs(i,j,table,visited)
                # dfs를 써서 3개 이상 연결된 조각이 있을 경우, 그 길이를 유물의 가치에 더해준다.
                if count >= 3:
                    total_value+=count
    return total_value
## main code








def dfs(y,x,table,visited,tracking_arr,count):
    # 1. 체크인
    visited[y][x] = True
    target_num = table[y][x]

    #2. 종료 조건인가?

    #3. 순회할 수 있는 곳 돌기
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        newy = y+dy[i]
        newx = x+dx[i]
        # 4. 방문할 수 있는가?
        if 0<=newy<5 and 0<=newx<5:
            if not visited[newy][newx] and table[newy][newx]==target_num:
                #5. 가자
                visited[newy][newx] = True
                count, tracking_arr = dfs(newy,newx,table,visited,tracking_arr+[(newy,newx)], count+1)
    #6. 체크아웃
    return count, tracking_arr

def get_treasures(table):
    # 탐색해서 얻어지는 유물이 없을 때 까지
    gotten_value = 0

    while True:
        # 1. 유물 탐색 하면서 조각 개수 누적하기, 유물이 된 조각은 0으로 만들기
        new_gotten_value = 0
        visited = [[False]*5 for _ in range(5)]
        tracking_arrs = []
        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    tracking_arr = []
                    count, tracking_arr = dfs(i,j,table, visited, tracking_arr,1)

                    if count >= 3:
                        tracking_arr.append((i,j)) # 시작 지점도 이제야 넣어주기
                        new_gotten_value += count
                        tracking_arrs += tracking_arr
                    # print("궁금해",i,j,"시작",count, tracking_arrs)
        
        # print("모아진 유물 가치는", new_gotten_value)
        # for arr in table:
        #     print(*arr)
        
        if new_gotten_value == 0:
            # print("count가 0입니다")
            break
        else:
            gotten_value += new_gotten_value

            # 유물 된 조각은 0으로 만들기, 0이 된 곳 채우기
            tracking_arrs.sort(key=lambda x:(x[1], -x[0]))
            # print(tracking_arrs)
            for y,x in tracking_arrs:
                table[y][x] = m_arr.popleft()

        # print("0으로 만들고 채운 table")
        # for arr in table:
        #     print(*arr)
        # print("---")

    return gotten_value, deepcopy(table)
        # if gotten_value == 0:
        #     # 더이상 얻어지는 유물이 없기 때문에 종료
        #     return 
    
    # 2. 0인 곳을 방문하면서 새로운 조각으로 채우기

# 1. 게임 시작
k,m = map(int, sys.stdin.readline().strip().split())
# k,m = 2,20

# 2. 테이블 만들기
table = []
for _ in range(5):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
# table = [[7, 6, 7, 6, 7], [6, 7, 6, 7, 6], [6, 7, 1, 5, 4], [7, 6, 3, 2, 1], [5, 4, 3, 2, 7]]
# table = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


# 3. 벽에 적힌 조각 번호
m_arr = deque(list(map(int, sys.stdin.readline().strip().split())))
# m_arr = deque([3, 2, 3, 5, 2, 4, 6, 1, 3, 2, 5, 6, 2, 1, 5, 6, 7, 1, 2, 3])


# 4. k번 턴 진행
for i in range(k):
    # print("this turn is", i)
    # a. 탐사 진행
    boxes = make_boxes(table)

    # 모든 candidates에 대해 유물 1차 획득 로직 돌기
    for candi in boxes:
        value = find_first_gotten_value(candi["table"])
        candi["value"] = value

    
    # b. 최종 테이블 고르기
    # 1차 유물 획득 가치가 최대인 테이블 확정 짓기
    boxes.sort(key= lambda x:(x["value"], -x["degree"], -x["center"][1], -x["center"][0]), reverse=True)
    # for box in boxes:
    #     print(box)
    chosen_table = boxes[0]["table"] 

    # 3. 최종 테이블에 대해 얻을 수 있는 유물 얻기(1차부터 다시)
    boxes[0]["value"] = 0

    result, gotten_table = get_treasures(chosen_table)
    if result != 0:
        print(result, end=" ")


    # 4. 다음 턴 진행을 위한 준비
    # 4-1. 최종 table을 탐사 시작 table로 명명
    table = gotten_table