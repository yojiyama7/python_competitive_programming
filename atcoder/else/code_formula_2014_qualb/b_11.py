N = input()

s = N[::-1]

odd, even = sum(map(int, s[::2])), sum(map(int, s[1::2]))

print(even, odd)