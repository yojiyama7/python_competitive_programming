N = int(input())
C = input()

a = [0]
b = [0]
for c in C:
    if c == "W":
        a.append(a[-1]+1)
    else:
        a.append(a[-1])
    if c == "R":
        b.append(b[-1]+1)
    else:
        b.append(b[-1])

# print(a, b)

# min_num = 10**18
# for i in range(N+1):
#     print(C[:i], C[i:])
#     print((a[i]-a[0]) - (b[N]-b[i]))
#     if a[i]-a[0] - b[N]-b[i] == 0:
#         min_num = min(a[i]-a[0], min_num)

# print(min_num)

def solve(x):
    r = (b[N]-b[x]) - (a[x]-a[0])
    # print(r)
    return r >= 0

# 右側のRの個数 - 左側のWの個数 >= 0 の最大
ok, ng = 0, N+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    # print(ok, ng, mid)
    if solve(mid):
        ok = mid
    else:
        ng = mid

# print(a, b)
# print(ok)

print(a[ok])

