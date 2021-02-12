from math import sqrt

A, B, C = map(int, input().split())

print("Yes" if 0 <= C-A-B and 4*A*B < (C-A-B)**2 else "No")
