N = int(input())
S = input()

if N%2:
    print(-1)
    exit()

ans = sum(a != b for a, b in zip(S[:N//2], S[N//2:]))
print(ans)
