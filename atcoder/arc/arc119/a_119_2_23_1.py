# N = a * 2^b + c
# (N - c)2^b = a

INF = 10**18

N = int(input())

ans = INF
for b in range(INF):
    x = 1<<b
    if x > N:
        break
    c = N%x
    a = N//x
    ans = min(ans, a+b+c)

print(ans)
