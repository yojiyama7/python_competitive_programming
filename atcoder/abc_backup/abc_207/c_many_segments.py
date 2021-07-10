N = int(input())
TLR = [list(map(int, input().split())) for _ in range(N)]

q = []
for t, l, r in TLR:
    if t == 1:
        q.append((l, r+0.1))
    elif t == 2:
        q.append((l, r))
    elif t == 3:
        q.append((l+0.1, r+0.1))
    else:
        q.append((l+0.1, r))

def is_overrap(p1, p2):
    l, r = p1
    a, b = p2
    if b <= l or r <= a:
        return False
    return True

# print(q)

ans = 0
for i, qi in enumerate(q):
    for qj in q[i+1:]:
        ans += is_overrap(qi, qj)
        # if is_overrap(qi, qj):
        #     print(i, j)

print(ans)
