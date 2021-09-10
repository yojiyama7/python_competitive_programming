A, B = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = """7 8 9 0
 4 5 6
  2 3
   1
"""

for p in P:
    ans = ans.replace(str(p), '.')
for q in Q:
    ans = ans.replace(str(q), 'o')
for i in range(10):
    ans = ans.replace(str(i), 'x')

print(ans)