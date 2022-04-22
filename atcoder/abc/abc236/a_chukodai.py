S = input()
A, B = map(int, input().split())

l = list(S)
l[A-1], l[B-1] = l[B-1], l[A-1]

ans = ''.join(l)
print(ans)