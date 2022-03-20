from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

A_acc_ri = 0
cnt = Counter()
cnt[0] = 1
ans = 0
for ri, a in enumerate(A):
    A_acc_ri += a
    # print((ri, a), cnt[A_acc_ri - K])
    ans += cnt[A_acc_ri - K]
    cnt[A_acc_ri] += 1

print(ans)
