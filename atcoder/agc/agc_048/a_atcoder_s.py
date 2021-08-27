INF = 10**18

T = int(input())

ac = "atcoder"
for _ in range(T):
    S = input()

    if S > ac:
        print(0)
        continue
    ans = INF
    for i in range(8):
        if S[:i] != ac[:i]:
            continue
        for j, c in enumerate(S[i:]):
            if c > ac[i]:
                ans = min(j, ans)
                break
    print(-1 if ans == INF else ans)
