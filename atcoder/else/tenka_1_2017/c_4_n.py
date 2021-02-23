# 分数を分数のまま式変形して a/b == c/d を b/a == d/c に変換

N = int(input())

for a in range(1, 3501):
    for b in range(1, 3501):
        num = a*b*N
        deno = 4*a*b - b*N - a*N
        # print(num, deno)
        if deno > 0 and num%deno == 0:
            print(a, b, num//deno)
            exit()
