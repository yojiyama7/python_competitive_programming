L, R = map(int, input().split())
S = input()

ans = S[:L-1] + S[L-1:R][::-1] + S[R:]
print(ans)