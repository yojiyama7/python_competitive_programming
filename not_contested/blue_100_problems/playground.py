
# INF = 10**18
# N = 20
# L = list(range(N, 2*N))

# # min(default=INF) -. 与えられた配列が空なら default をかえす
# print(min(L, default=INF))

################################

N = 20
L = [set() for i in range(N)]

for i in range(N):
    for j in range(5):
        L[i].add(i+j*5)

print(L)
for i in range(N):
    # これなに -> set to list
    *L[i], = L[i]
print(L)
