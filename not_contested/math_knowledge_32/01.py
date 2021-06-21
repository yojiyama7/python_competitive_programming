# A の要素のうち 整数, 非負整数, 自然数 であるものを答えよ

A = {-5, -4.5, -2, 0, 4, 6}

print("整数")
print([a for a in A if a % 1 == 0])
print("非負整数")
print([a for a in A if not a < 0])
print("自然数")
print([a for a in A if a > 0])
