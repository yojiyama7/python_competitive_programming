N = int(input())
LA = [tuple(map(int, input().split())) for _ in range(N)]

print(len(set(LA)))