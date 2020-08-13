N = int(input())
A = [input() for _ in range(N)]

s = list(map(set, A))

def solve():
    t = ""
    for i in range(N//2):
        g = s[i] & s[-(i+1)]
        if g:
            t += list(g)[0]
        else:
            return -1
    if N%2:
        center = list(s[N//2])[0]
        return t + center + t[::-1]
    return t + t[::-1]

print(solve())