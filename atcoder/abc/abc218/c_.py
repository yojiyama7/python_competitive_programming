INF = 10**18

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

def strip(s):
    xmin, xmax = INF, -INF
    ymin, ymax = INF, -INF
    for y, line in enumerate(s):
        for x, c in enumerate(line):
            if c == '#':
                xmin = min(x, xmin)
                xmax = max(x, xmax)
                ymin = min(y, ymin)
                ymax = max(y, ymax)
    return [line[xmin:xmax+1] for line in s[ymin:ymax+1]]

def rotate90(x):
    ans = [''.join(xzip_i)[::-1] for xzip_i in zip(*x)]
    return ans

# def rotate90(x):
#     return list(map(list, zip(*x[::-1])))

s = strip(S)
t = strip(T)
for i in range(4):
    if s == t:
        print("Yes")
        exit()
    s = rotate90(s)

print("No")
