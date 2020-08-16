# 理解が足りない 雰囲気はわかる
# ただのN進数変換では。(Nが負の数ではあるが)

N = int(input())

if N == 0:
    print(0)
    exit()

t = ""
while N:
    r = N%2
    N = (N - r) // (-2)
    t += str(r)

print(t[::-1])
