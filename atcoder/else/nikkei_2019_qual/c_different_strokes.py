# 数学考察むずい

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = zip(*AB)

score = -sum(B)

a_add_b = [a+b for a, b in AB]
a_add_b.sort(reverse=True)

score += sum(a_add_b[::2])

print(score)