# 各ケースにおいて貪欲っぽい？L[i]-R[i]をスコアとしてk[i]でくくってk[i]の小さい順にqに追加する

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

T = int(input())

for i in range(T):
    N = int(input())
    KLR = [list(map(int, input().split())) for _ in range(N)]

    items = [set() for _ in range(N)]
    for k, l, r in KLR:
        items[k].add(L-R)

    q = HeapQueue([])
    for i in range(N):

