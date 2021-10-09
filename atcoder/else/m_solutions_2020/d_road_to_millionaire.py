INF = 10**18

N = int(input())
A = list(map(int, input().split()))

l = []
ba = None
for a in A:
    if ba != a:
        l.append(a)
    ba = a

l = [INF] + l + [-INF]

money = 1000
kabu = 0
for i in range(1, len(l)-1):
    if l[i-1] < l[i] > l[i+1]:
        money += kabu*l[i]
        kabu = 0
    if l[i-1] > l[i] < l[i+1]:
        kabu += money//l[i]
        money %= l[i]
    # print(money, kabu)

print(money)