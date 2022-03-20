N, X = map(int, input().split())

if N == 2:
    if X == 2:
        print("Yes")
        print(*[1, 2, 3])
    else:
        print("No")
    exit()

c = N-1
ans = None
if 1 <= X-2 and X+1 <= 2*N-1:
    ans = [None]*(2*N-1)
    ans[c+1] = X-1
    ans[c] = X
    ans[c-1] = X+1
    ans[c-2] = X-2
    l = list(range(1, X-2)) + list(range(X+2, 2*N))
    ans[:c-2] = l[:c-2]
    ans[c+2:] = l[c-2:]
elif 1 <= X-1 and X+2 <= 2*N-1:
    ans = [None]*(2*N-1)
    ans[c+1] = X+1
    ans[c] = X
    ans[c-1] = X-1
    ans[c-2] = X+2
    l = list(range(1, X-1)) + list(range(X+3, 2*N))
    ans[:c-2] = l[:c-2]
    ans[c+2:] = l[c-2:]

if ans:
    print("Yes")
    print(*ans)
else:
    print("No")