from functools import cmp_to_key

INF = 10**9+1

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def create_frac(p, q):
    if q == 0:
        return (INF, 1)
    return (p, q)

def compare(a, b):
    # print(a, b)
    p1, q1 = a
    p2, q2 = b
    a_score, b_score = p1*q2, p2*q1
    if a_score < b_score:
        return -1
    if a_score > b_score:
        return 1
    return 0

sections = []
for x, y in XY:
    a, b = x, y-1
    start = create_frac(b, a)
    a, b = x-1, y
    end = create_frac(b, a)
    sections.append((start, end))

def sort_key(sec1, sec2):
    # print([sec1[1], sec2[1]])
    return compare(sec1[1], sec2[1])

sections.sort(key=cmp_to_key(sort_key))
ans = 0
b_end = (0, 1)
for start, end in sections:
    if compare(start, b_end) == -1:
        continue
    ans += 1
    b_end = end

print(ans)
