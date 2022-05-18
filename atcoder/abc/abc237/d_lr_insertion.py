from collections import deque

N = int(input())
S = input()

q = deque([N])
for n, c in reversed(list(enumerate(S))):
    if c == 'L':
        q.append(n)
    else:
        q.appendleft(n)

print(*q)