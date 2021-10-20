N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = zip(*AB)

times = [a/b for a, b in AB]

times_sum = sum(times)

s = 0
idx = None
for idx, t in enumerate(times):
    if s + t > times_sum / 2:
        break
    s += t

remain_time = (times_sum / 2 - s)
remain_res = remain_time / times[idx]
ans = sum(A[:idx]) + A[idx]*remain_res

print(ans)