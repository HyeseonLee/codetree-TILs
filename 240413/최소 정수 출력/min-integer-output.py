import sys
import heapq

n = int(sys.stdin.readline().strip())
arr = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    
    if num>0: # 자연수
        # 배열에 자연수 넣기 (이때 배열을 우선순위큐로 사용해야해)
        heapq.heappush(arr, num)
    elif num == 0: # 0이라면
        if len(arr)==0:
            # arr이 비어있다면
            print(0)
        else:
            # arr에서 가장 작은 값 출력&제거
            print(heapq.heappop(arr))