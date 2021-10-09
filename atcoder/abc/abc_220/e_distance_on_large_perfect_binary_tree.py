MOD = 998244353

N, D = map(int, input().split())

ans = 0
for i in range(N):
    x = 0
    if i+D < N:
        x += pow(2, D, MOD) * 2
        # print((i, ), pow(2, D, MOD) * 2)
        x %= MOD
    if D >= 2:
        a_max = min(N-1-i, D-1)
        a_min = D-a_max
        # print((i,), [a_min, a_max])
        if a_min <= a_max:
            x += pow(2, D-2, MOD) * 2 * (a_max - a_min + 1)
            # print((i,), [a_min, a_max], pow(2, D-2, MOD) * 2 * (a_max - a_min + 1))
            x %= MOD
    x *= pow(2, i, MOD)
    x %= MOD
    ans += x
    ans %= MOD
    # print(x, ans)
    

print(ans)

################################

# MOD = 10**9+7

# N, D = map(int, input().split())

# ans = 0
# b_ans = 0
# for i in range(N):
#     if i+D < N:
#         ans += (D-1) * pow(2, D, MOD)
#         ans %= MOD
#     else:
#         x, y = D+i-N, min(D, N-i)
#         ans += (y-x) * pow(2, D, MOD)
#         ans %= MOD
#     print(i, ans-b_ans)
#     b_ans = ans

# print(ans)

################################

# # NO SUB

# MOD = 998244353

# N, D = map(int, input().split())

# ans = 0
# for i in range(N):
#     a_max = min(D, N-i-1)
#     a_min= max(0, D - a_max)

#     if a_min > a_max:
#         break
#     ans += (a_max-a_min+1) * pow(2, D, MOD)
#     ans %= MOD
#     print(i, (a_min, a_max), ans)

# print(ans)

################################

# ans = 0
# for i in range(N-D):
#     ans += pow(2, i+D, MOD)

# print(ans)

# for a in range(1, D):
#     b = D-a
#     x = pow(2, a-1, MOD)
#     y = pow(2, b-1, MOD)
#     ans += x*y
#     ans %= MOD
#     print((a, b), ans)

# print(ans)