# 実装力の低下を観測。
# 実装に入る前に考察を固めた方が良いことを発見。
from itertools import groupby

S = input()
K = int(input())

def count(nums):
    return sum(num//2 for num in nums)

l = [len(list(g)) for k, g in groupby(S)]

if len(l) == 1:
    print(l[0]*K//2)
elif S[0] == S[-1]:
    print(count(l)*K - (count([l[0]]) + count([l[-1]]) - count([l[0]+l[-1]]))*(K-1))
else:
    print(count(l)*K)