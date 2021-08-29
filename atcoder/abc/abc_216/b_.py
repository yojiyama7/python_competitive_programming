N = int(input())
ST = [input() for _ in range(N)]

if len(set(ST)) == N:
    print("No")
else:
    print("Yes")
