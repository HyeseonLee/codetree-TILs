import sys 
import heapq

n = int(sys.stdin.readline().strip())

class PriorityQueue:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def empty(self):
        return not self.items
    def push(self, x):
        heapq.heappush(self.items, -x)
    def top(self):
        if self.empty():
            return Exception("empty")
        else:
            return -self.items[0]
    def pop(self):
        if self.empty():
            return Exception("empty")
        else:
            return -heapq.heappop(self.items)

pq = PriorityQueue()

for _ in range(n):
    line = sys.stdin.readline().strip().split()
    if line[0] == "push":
        pq.push(int(line[1]))
    elif line[0] == "pop":
        print(pq.pop())
    elif line[0] == "size":
        print(pq.size())
    elif line[0] == "empty":
        print(1 if pq.empty() else 0)
    elif line[0] == "top":
        print(pq.top())