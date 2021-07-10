# 最大2部マッチング問題
# or 事前に整理してあげる貪欲(むしろそれがただの貪欲では)
# なぜこれでいいのかいまいち。数学やれ案件。

N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]
CD = [list(map(int, input().split(" "))) for _ in range(N)]

CD.sort()
AB.sort(key=lambda x: (x[1], x[0]), reverse=True)

count = 0
for c, d in CD:
    for j, (a, b) in enumerate(AB):
        if a < c and b < d:
            count += 1
            AB.pop(j)
            break

print(count)