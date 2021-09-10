N = int(input())
A = list(map(int, input().split()))

l = sorted((a*N, i) for i, a in enumerate(A))

avg = sum(A)
min_diff = min(abs(la-avg) for la, li in l)

# print(l)

p = [li for la, li in l if abs(la-avg) == min_diff]

print(min(p))
