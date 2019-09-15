N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

l = [0]*(N+1)
for a in A:
    l[a] += 1

for i in range(1, N+1):
    if Q-l[i] < K:
        print("Yes")
    else:
        print("No")