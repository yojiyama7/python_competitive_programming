# わからな強すぎ
# よく俺このコード書けたな
# エラトステネスの篩 O(N log log N) らしいです

INF = 10**7

L, R = map(int, input().split())

l = [None]*(R+1)
ans = 0
# gcd(x, y) == i となるものを数える
for i in reversed(range(2, R+1)):
    l[i] = (R//i - (L-1)//i)**2
    for j in range(2, INF):
        if i*j > R:
            break
        l[i] -= l[i*j]
    ans += l[i]

# x == g or y == g を引く
for i in range(2, R+1):
    if L <= i <= R:
        ans -= 2*(R//i - (L-1)//i) - 1

print(ans)
