N = int(input())
A = list(map(int, input().split()))

l = [(a, i+1) for i, a in enumerate(A)]
for i in range(N-1):
    l_next = []
    for j in range(len(l)//2):
        winner = max(l[2*j], l[2*j+1])
        l_next.append(winner)
    l = l_next

print(min(l)[1])
