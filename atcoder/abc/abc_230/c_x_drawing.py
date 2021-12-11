N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

AB_slash = A+B
AB_back_slash = A-B

m = [[0 for _ in range(R, S+1)] for _ in range(P, Q+1)]
for i in range(P, Q+1):
    for j in range(R, S+1):
        slash = i+j
        back_slash = i-j
        if slash == AB_slash or back_slash == AB_back_slash:
            m[i-P][j-R] = 1

for mi in m:
    t = ''.join(".#"[v] for v in mi)
    print(t)

