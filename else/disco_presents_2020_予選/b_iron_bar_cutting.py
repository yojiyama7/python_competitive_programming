N = int(input())
A = list(map(int, input().split()))

left_to_me = [0]*(N+1)
for i, a in enumerate(A):
    left_to_me[i+1] = left_to_me[i]+a

right_to_me = [0]*(N+1)
for i in range(N-1, -1, -1):
    right_to_me[i-1] = right_to_me[i]+A[i]

min_cost = 10**24
for i, a in enumerate(A):
    target = abs(left_to_me[i]-right_to_me[i])
    cost = abs(target-a)
    min_cost = min(min_cost, cost)

print(min_cost)