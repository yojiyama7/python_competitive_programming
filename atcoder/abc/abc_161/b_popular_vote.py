N, M = map(int, input().split())
A = list(map(int, input().split()))

A_sum = sum(A)

this_or_more = A_sum/(4*M)

print("Yes" if sum(a>=this_or_more for a in A) >= M else "No")