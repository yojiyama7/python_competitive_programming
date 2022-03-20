K = int(input())

ans = 0
for a in range(1, K+1):
    for b in range(1, -(-K//a)+1):
        lim = K//(a*b)
        ans += lim
print(ans)
