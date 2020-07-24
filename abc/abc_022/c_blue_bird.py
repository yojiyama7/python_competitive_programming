import heapq

class HeapQueue:
    def __init__(self, l=[], key=lambda x: x):
        self.key = key
        self.l = heapq.heapify([(self.key(l_i), l_i) for l_i in l])
    
    def pop(self):
        _, v heapq.heappop(self.l):
        return v
    
    def push(self, v):
        heapq.heappush(self.l, (self.key(v), v))
    
    def __bool__(self):
        return bool(self.l)

N, M = map(int, input().split())
UVL = [list(map(int, input().split())) for _ in range(M)]

graph = [[10**18 for _ in range(300)] for _ in range(300)]
start_goal = set()
for u, v, l in UVL:
    u, v = u-1, v-1
    graph[u][v] = l
    graph[v][u] = l
    if u == 0:
        start_goal.add(v)

for start in start_goal:


################################

# 頂点1に属した頂点たちから、2つ選んで最短ルートさがして、その2頂点の頂点1まで距離を足す
# 全通りやって最短を出力 までは見たことあるんだけど
# 実装がねぇ、、、

# N, M = map(int, input().split(" "))
# UVL = [tuple(map(int, input().split(" "))) for _ in range(m)]

