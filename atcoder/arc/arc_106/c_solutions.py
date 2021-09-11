N, M = map(int, input().split())

if M < 0:
    print(-1)
    exit()

s, e = 10, 10**6

ans = [(s, e)]

if M >= 1:
    for i in range(M+1):
        l, r = s+1, s+1
        l += i*2
        r += i*2+1
        ans.append((l, r))

if len(ans) > N:
    print(-1)
    exit()

for i in range(N-len(ans)):
    l, r = e+1, e+1
    l += i*2
    r += i*2+1
    ans.append((l, r))

for l, r in ans:
    print(l, r)

################################

# # NON SUB

# N, M = map(int, input().split())

# s, e = 10, 10**6

# ans = [(s, e)]

# if M == 0:
#     pass
# if M < 0:
#     ans.append((e-1, e+1))
# else:
#     ans.append((s-1, s+1))

# for i in range(abs(M)):
#     l, r = s+2, s+2
#     l += 2*i
#     r += 2*i + 1
#     ans.append((l, r))

# if len(ans) > N:
#     print(-1)
#     exit()

# for i in range(N - len(ans)):
#     l, r = e+2, e+2
#     l += 2*i
#     r += 2*i + 1
#     ans.append((l, r))

# for l, r in ans:
#     print(l, r)