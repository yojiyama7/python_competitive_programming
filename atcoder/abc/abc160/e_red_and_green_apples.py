from heapq import *

X, Y, A, B, C = list(map(int, input().split()))
PQR = [list(map(int, input().split())) for _ in range(3)]

def to_heap(l):
    l = [(-x, x) for x in l]
    heapify(l)
    return l

apples = [to_heap(l + [-1]) for l in PQR]
apple_count = [0, 0, 0]
sum_num = 0
while sum(apple_count) < (X + Y):
    if apple_count[0] == X:
        apples[0] = [(1, -1)]
    if apple_count[1] == Y:
        apples[1] = [(1, -1)]
    max_apple_index = max(range(3), key=lambda x: apples[x][0][1])
    sum_num += apples[max_apple_index][0][1]
    heappop(apples[max_apple_index])
    apple_count[max_apple_index] += 1

print(sum_num)