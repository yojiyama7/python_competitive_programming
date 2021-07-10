# 第一条件を満たすもの - 第一条件を満たすが第二条件を満たさないもの
# 扱いづらい条件は逆にして扱うと良い。

# DPを使ってできるかどうか


from collections import Counter

N = int(input())
S = input()

counter = Counter(S)

r = 1
for c in "RGB":
    r *= counter[c]

for i in range(N):
    for j in range(i+1, N):
        k = 2*j-i
        # print(i, j, k)
        if k < N and len({S[i], S[j], S[k]}) == 3:
            r -= 1

print(r)