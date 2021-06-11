from collections import deque

S = input()

q = deque([])

is_filp = 0
for s in S:
    if s == 'R':
        is_filp += 1
        is_filp %= 2
    else:
        if q:
            if is_filp:
                x = q.popleft()
                if x != s:
                    q.appendleft(x)
                    q.appendleft(s)
            else:
                x = q.pop()
                if x != s:
                    q.append(x)
                    q.append(s)
        else:
            q.append(s)

t = "".join(q)
if is_filp:
    t = t[::-1]

print(t)
