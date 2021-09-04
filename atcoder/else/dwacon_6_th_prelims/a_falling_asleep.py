N = int(input())
ST = [input().split() for _ in range(N)]
X = input()

ST = [(s, int(t)) for s, t in ST]
S, T = zip(*ST)
T_sum = sum(T)
diff = 0
for s, t in ST:
    diff += t
    if s == X:
        break

print(T_sum-diff)
