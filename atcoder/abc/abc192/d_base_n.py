X = input()
M = int(input())

def base(x, n):
    sum_num = 0
    for i, x_i in enumerate(x[::-1]):
        sum_num += n**i * int(x_i)
    return (sum_num)

def solve(n):
    return (base(X, n) <= M)

if len(X) == 1:
    print(1 if int(X) <= M else 0)
    exit()

ok = 10
ng = 10**20
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

cnt = 0
for i in range(max(map(int, X))+1, 11):
    cnt += solve(i)

# print(cnt)

print(ok - 10 + cnt)
