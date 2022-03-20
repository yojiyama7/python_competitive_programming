P = list(map(int, input().split()))

table = ""
for i in range(26):
    table += chr(ord('a') + i)
ans = ""
for p in P:
    ans += table[p-1]

print(ans)

################################

# P = list(map(int, input().split()))

# l = [p-1 for p in P]
# ans = ''.join(chr(ord('a') + li) for li in l)
# print(ans)
