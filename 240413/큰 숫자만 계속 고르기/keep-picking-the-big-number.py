import sys
import heapq

n,m = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
pq = []

for x in lst: # O(N)
    heapq.heappush(pq, -x)

for _ in range(m): # O(N)
    max_num = -heapq.heappop(pq)
    heapq.heappush(pq, -(max_num-1))

print(-pq[0])