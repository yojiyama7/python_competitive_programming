N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

a, b = max(AB)

print(a+b)