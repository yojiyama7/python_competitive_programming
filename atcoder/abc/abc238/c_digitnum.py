MOD = 998244353

# cnt[i]: 1 <= x <= N で桁数がiであるもの数
# sum(c*(c+1)//2 for c in cnt)

N = int(input())

cnt = [0]*19
for i in range(19):
    if i == 0:
        continue
    start = 10**(i-1)
    if start > N:
        break
    ok, ng = start, N+1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if len(str(mid)) <= i:
            ok = mid
        else:
            ng = mid
    # print((ok, ng), start)
    cnt[i] = max(0, ok-start+1)

# print(cnt)

ans = 0
for c in cnt:
    score = c*(c+1)//2
    ans += score
    ans %= MOD

print(ans)