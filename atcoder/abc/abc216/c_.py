N = int(input())

x = bin(N)[2:]
ans = ""
for c in x:
    ans += 'B'
    if c == '1':
        ans += 'A'

print(ans)

################################

# N = int(input())

# ans = ""
# x = N
# while x:
#     if x%2 == 1:
#         ans += "A"
#     x //= 2
#     ans += "B"

# print(ans[::-1])
