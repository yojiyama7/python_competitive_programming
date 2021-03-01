from itertools import chain
from collections import Counter

H, W = map(int, input().split())
A = [input() for _ in range(H)]

def solve():
    x4 = (H//2)*(W//2)
    x2 = 0 
    if H%2:
        x2 += W//2
    if W%2:
        x2 += H//2
    # print(x4, x2)

    cnt2 = 0
    cnt4 = 0
    for v in Counter(chain(*A)).values():
        cnt4 += v//4
        cnt2 += (v%4)//2
    # print(cnt2, cnt4)
    if x4 > cnt4:
        return (False)
    cnt4 -= x4
    cnt2 += 2*cnt4
    # print(cnt2, cnt4)
    if x2 > cnt2:
        return (False)
    return (True)

print("Yes" if solve() else "No")
