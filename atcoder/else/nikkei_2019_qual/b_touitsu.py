N = int(input())
A = input()
B = input()
C = input()

ans = sum(len({A[i], B[i], C[i]})-1 for i in range(N))
print(ans)