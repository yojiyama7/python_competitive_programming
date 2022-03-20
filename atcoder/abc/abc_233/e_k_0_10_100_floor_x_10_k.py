X = input()

N = len(X)

sum_digits = [0]*(N+1)
for i in range(N):
    sum_digits[i+1] = sum_digits[i] + int(X[i])

ans_digits = [0]*N
carry = 0
for i in range(N):
    carry, s = divmod(sum_digits[N-i] + carry, 10)
    ans_digits[i] = s

# print(carry, ans_digits[::-1])

ans_str = (str(carry) if carry else '') + ''.join(map(str, ans_digits[::-1]))
print(ans_str)

################################

# X = input()

# X_len = len(X)

# memo = [None]*(X_len+1)
# def sum_digits(r0x):
#     if r0x == 0:
#         return 0
#     if memo[r0x] == None:
#         memo[r0x] = sum_digits(r0x-1) + int(X[r0x-1])
#     return memo[r0x]

# ans = []
# mem = 0
# for i in range(X_len+10):
#     score = mem + sum_digits

################################

# INF = 10**18

# X = input()

# X_len = len(X)
# digit_btwns = [[0]*10 for _ in range(X_len+1)]

# for i, x in enumerate(X[::-1]):
#     x = int(x)
#     digit_btwns[0][x] += 1
#     digit_btwns[i+1][x] -= 1

# cnts_maxidx = X_len
# cnts = [[0]*10 for _ in range(500010)]
# ans_digits = ['0']*500010
# for i in range(500010):
#     if i > cnts_maxidx:
#         break
#     if i >= 1:
#         for j in range(10):
#             cnts[i][j] += cnts[i-1][j]
#     if i < X_len+1:
#         for j in range(10):
#             cnts[i][j] += digit_btwns[i][j]
#     score = 0
#     for j in range(10):
#         score += cnts[i][j]*j
#     score_str = str(score)[::-1]
#     ans_digits[i] = score_str[0]
#     for j, sc in enumerate(score_str[1:], start=1):
#         m = int(sc)
#         cnts[i+j][m] += 1
#         cnts_maxidx = max(cnts_maxidx, i+j)
