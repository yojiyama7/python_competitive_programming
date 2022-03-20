from collections import Counter

N, K = map(int, input().split())
C = list(map(int, input().split()))

cnt = Counter(C[:K])
score = len(cnt.keys())
ans = score
for i in range(N-K):
    # print(cnt, score)
    cnt[C[i]] -= 1
    if cnt[C[i]] == 0:
        score -= 1
    if cnt[C[i+K]] == 0:
        score += 1
    cnt[C[i+K]] += 1
    ans = max(score, ans)

print(ans)

