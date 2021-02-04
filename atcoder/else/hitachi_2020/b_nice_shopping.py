A_len, B_len, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
XYC = [list(map(int, input().split())) for _ in range(M)]

min_num = min(A) + min(B)
for x, y, c in XYC:
    x, y, c = x-1, y-1, c
    score = A[x] + B[y] - c
    min_num = min(min_num, score)

print(min_num)
