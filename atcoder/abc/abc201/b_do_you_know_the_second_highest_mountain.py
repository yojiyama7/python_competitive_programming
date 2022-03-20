N = int(input())
ST = [[f(v) for v, f in zip(input().split(), [str, int])] for _ in range(N)]

ST.sort(key=(lambda x: x[1]), reverse=True)
print(ST[1][0])