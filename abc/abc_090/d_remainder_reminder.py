# なぜか分からない、一時的なものだと思いさんぽへGO。

# N, K = map(int, input().split())

# # 1からnまででkで割った余りがp以上のkの個数
# def f(b):
#     print(b, (N//b, max(0, b-K+1)), max(0, (N%b)-K+1))
#     return (N//b)*max(0, b-K+1) + max(0, (N%b)-K+1)

# c = 0
# for b in range(1, N+1):
#     c += f(b)

# print(c)