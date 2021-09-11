P = list(map(int, input().split()))

l = [p-1 for p in P]
ans = ''.join(chr(ord('a') + li) for li in l)
print(ans)