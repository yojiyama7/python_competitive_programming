INF = 10**18

P = int(input())

l = [1]
for i in range(1, INF):
    x = l[-1]*i
    if x > P:
        break
    l.append(x)

ans = 0
for x in l[::-1]:
    ans += P//x
    P %= x

print(ans)
INF = 10**18

P = int(input())

l = [1]
for i in range(1, INF):
    x = l[-1]*i
    if x > P:
        break
    l.append(x)

ans = 0
for x in l[::-1]:
    ans += P//x
    P %= x

print(ans)
