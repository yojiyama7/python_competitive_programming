x, y = map(int, input().split())

if x == y:
    print(x)
else:
    s = set(range(3)) - {x} - {y}
    print(s.pop())
