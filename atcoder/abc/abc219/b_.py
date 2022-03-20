S = [input() for _ in range(3)]
T = input()

ans = ''.join(S[int(t)-1] for t in T)

print(ans)
