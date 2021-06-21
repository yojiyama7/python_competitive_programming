S = "1101010000110000000011010100001100000000"

ans = 0
for i, s in enumerate(S[::-1]):
    ans += 2**i * int(s)

print(ans)
# print(int(S, 2))