N, M, Q = list(map(int, input().split()))
S = [input().split() for _ in range(Q)]

solved_list = [[] for _ in range(N)]
problems = [N]*N

for s in S:
    if s[0] == "1":
        n = int(s[1])-1
        print(sum([problems[solved] for solved in solved_list[n]]))
    elif s[0] == "2":
        n, m = int(s[1])-1, int(s[2])-1
        solved_list[n].append(m)
        problems[m] -= 1