N = int(input())
TKA = [list(map(int, input().split())) for _ in range(N)]

visited = [0 for _ in range(N)]
visited[N-1] = 1
q = [N-1]
ans = 0
while q:
    this = q.pop()
    t, k, *a = TKA[this]
    ans += t
    for ai in a:
        ai -= 1
        if visited[ai]:
            continue
        visited[ai] = 1
        q.append(ai)

print(ans)
