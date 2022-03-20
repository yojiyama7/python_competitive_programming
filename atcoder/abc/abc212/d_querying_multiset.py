from heapq import *

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

hq = HeapMin()
adjust = 0
for query in QUERY:
    if query[0] == 1:
        t, x = query
        hq.push(x-adjust)
    elif query[0] == 2:
        t, x = query
        adjust += x
    else:
        t = query[0]
        print(hq.pop()+adjust)
