from collections import deque

S = input()

q = deque(S)

r = 0
while q and q[-1] == 'a':
    q.pop()
    r += 1
l = 0
while q and q[0] == 'a':
    q.popleft()
    l += 1

p = list(q)
if l <= r and p == p[::-1]:
    print("Yes")
else:
    print("No")
