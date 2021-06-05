# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = map(list, zip(*AB))

A.sort()
B.sort()
cost = sum(abs(a - A[N//2]) for a in A)
cost += sum(abs(b - B[N//2]) for b in B)
cost += sum(abs(a - b) for a, b in AB)

print(cost)
