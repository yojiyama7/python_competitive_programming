from bisect import bisect

N, H = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = zip(*AB)
B = sorted(B)

max_A = max(A)
knifes = B[bisect(B, max_A):]

count = 0
while H > 0 and knifes:
    H -= knifes.pop()
    count += 1
if H > 0:
    count += -(-H//max_A)

print(count)