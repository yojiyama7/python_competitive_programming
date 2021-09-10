from math import ceil

X, Y, Z = map(int, input().split())

print(ceil((Y/X)*Z)-1)
