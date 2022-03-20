N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

l = [tuple(c[i+1] - c[i] for i in range(N-1)) for c in C]
if len(set(l)) != 1:
    print("No")
    exit()

C0_min = min(C[0])
ans_a = [min(c) for c in C]
ans_b = [x - C0_min for x in C[0]]
print("Yes")
print(*ans_a)
print(*ans_b)
