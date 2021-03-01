MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

# 順不同(?)
xyz = [0, 0, 0]
score = 1
for a in A:
    score *= xyz.count(a)
    score %= MOD
    if a in xyz:
        xyz[xyz.index(a)] += 1

print(score)
