# DPで解いてみたい。

N = int(input())

# 素数^a, 素数^b, 素数^c
# print((a+1)*(b+1)*(c+1) = 約数の数)

# p = [2]
# for i in range(3, 101):
#     if any(i % p_i == 0 for p_i in p):
#         continue
#     p.append(i)
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# print(p)

l = [0]*101
for i in range(2, N+1):
    for p_i in p:
        while i % p_i == 0:
            i //= p_i
            l[p_i] += 1
# print(l[:N+1])

# (3, 5, 5), (15, 5), (3, 25), (75)


def e(m):
    return sum(l_i >= m-1 for l_i in l)

# WHYYYYYYYYYYYY.
# Nの素因数分解から、Nの約数のうち、約数の個数がMになるものを求める数式
print(e(75) + e(25) * (e(3) - 1) + e(15) * (e(5) - 1) +
      e(5) * (e(5) - 1) * (e(3) - 2) // 2)
