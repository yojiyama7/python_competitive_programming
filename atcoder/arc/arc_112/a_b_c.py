T = int(input())

def f(a, b):
    if a == 0:
        return (b*(b+1))//2
    return f(0, b) - f(0, a-1) 

for _ in range(T):
    L, R = map(int, input().split())

    w = R-L+1

    cl, cr = L, R-L
    if cl > cr:
        print(0)
        continue
    cw = cr-cl+1
    ans = w*cw - f(cl, cr)
    print(ans)
