# combination を計算せず比較することができるか
# というより、nCkの nが最大だけ見ればいいらしいぞ　知らんけど

################################

N = int(input())
A = list(map(int, input().split()))

*else_A, max_A = sorted(A)

print(max_A, min(else_A, key=lambda a: abs(max_A/2 - a) ))