from itertools import accumulate as acc

S = input()
K = int(input())

S_len = len(S)

cost = [s == '.' for s in S]
cost_acc = [0] + list(acc(cost))

ans = 0
r = 0
for l in range(S_len):
    r = max(l, r)
    while r < S_len and cost_acc[r+1] - cost_acc[l] <= K:
        r += 1
    ans = max(r-l, ans)

print(ans)
