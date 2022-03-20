X = input()
N = int(input())
S = [input() for _ in range(N)]

d = dict((x, i) for i, x in enumerate(X))

def f(x):
    l = [d[xi] for xi in x]
    ans = ''.join(chr(li) for li in l)
    return ans

# l = [(f(s), s) for s in S]
# l.sort()
# for _, li in l:
#     print(li)

ans = sorted(S, key=f)
print(*ans, sep='\n')
