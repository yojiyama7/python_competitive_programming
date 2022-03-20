from heapq import *
from collections import deque

class HeapMin:
    def __init__(self, l=[], key=lambda x:x):
        self.key = key
        self.l = [(self.key(l_i), l_i) for l_i in l]
        heapify(self.l)

    def push(self, v):
        heappush(self.l, (self.key(v), v))

    def pop(self):
        _, r = heappop(self.l)
        return r

    def __bool__(self):
        return len(self.l) > 0

Q = int(input())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

p = deque()
hq = HeapMin()
for query in QUERY:
    t = query[0]
    if t == 1:
        x = query[1]
        p.append(x)
    elif t == 2:
        if hq:
            print(hq.pop())
        else:
            print(p[0])
            p.popleft()
    elif t == 3:
        for pi in p:
            hq.push(pi)
        p = deque()
