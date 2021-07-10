from fractions import Fraction

N = int(input())
A = list(map(int, input().split(" ")))

print(float(1/sum([Fraction(1, a) for a in A])))
