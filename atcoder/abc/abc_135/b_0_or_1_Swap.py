N = int(input())
P = list(map(int, input().split(" ")))

q = sorted(P)

if sum(p_i!=q_i for p_i, q_i in zip(P, q)) <= 2:
    print("YES")
else:
    print("NO")