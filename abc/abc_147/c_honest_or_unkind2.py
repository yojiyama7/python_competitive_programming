N = int(input())
XY_LIST = [[list(map(int, input().split())) for _ in range(int(input()))] for _ in range(N)]

def count_honest(i):
    l = [(i>>j)%2 for j in range(N)]
    for j in range(N):
        if (i>>j)%2 == 0:
            continue
        for x, y in XY_LIST[j]:
            x = x-1
            if l[x] == y:
                continue
            return 0
    return sum(l)

max_honest = 0
for i in range(1<<N):
    honest = count_honest(i)
    max_honest = max(max_honest, honest)

print(max_honest)


        