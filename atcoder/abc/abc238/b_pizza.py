N = int(input())
A = list(map(int, input().split()))

s = {0}
x = 0
for a in A:
    x += a
    x %= 360
    s.add(x)

l = sorted(s)
ans = 0
for i in range(len(l)):
    a, b = l[i], l[(i+1)%len(l)]
    size = (b-a)%360
    ans = max(size, ans)

print(ans)