from heapq import *

class HeapMin:
    def __init__(self, l):
        self.l = l
        heapify(self.l)

    def pop(self):
        return heappop(self.l)

    def push(self, v):
        heappush(self.l, v)
