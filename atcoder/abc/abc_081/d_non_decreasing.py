# 最小手数ではないので。はい。問題をしっかり把握しようね。

N = int(input())
A = list(map(int, input().split()))

s = []

min_Ai, *_, max_Ai = sorted(range(N), key=lambda x: A[x])
min_A, max_A = A[min_Ai], A[max_Ai]
if abs(min_A) < abs(max_A):
    for i in range(N):
        if i == max_Ai:
            continue
        A[i] += max_A
        s.append((max_Ai, i))
    A[max_Ai] += max_A
    s.append((max_Ai, max_Ai))
    # print(A)
    for i in range(N-1):
        if A[i] > A[i+1]:
            A[i+1] += A[i]
            s.append((i, i+1))
else:
    for i in range(N):
        if i == min_Ai:
            continue
        A[i] += min_A
        s.append((min_Ai, i))
    A[min_Ai] += min_A
    s.append((min_Ai, min_Ai))
    # print(A)
    for i in range(N-2, -1, -1):
        if A[i] > A[i+1]:
            A[i] += A[i+1]
            s.append((i+1, i))

print(len(s))
for a, b in s:
    print(a+1, b+1)




