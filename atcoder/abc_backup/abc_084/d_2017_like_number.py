# エラトステネスの篩ですねはい。

from bisect import bisect_left, bisect_right

Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

prime_flags = [1]*(10**5+1)
prime_flags[1] = 0
for i in range(2, 10**5+1):
    if prime_flags[i] == 0:
        continue
    for j in range(2*i, 10**5+1, i):
        prime_flags[j] = 0

num2017s = []
for i in range(1, 10**5+1, 2):
    if prime_flags[i] == prime_flags[(i+1)//2] == 1:
        num2017s.append(i)

for l, r in LR:
    print(bisect_right(num2017s, r) - bisect_left(num2017s, l))
