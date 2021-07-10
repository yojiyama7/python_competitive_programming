N = int(input())
S = list(map(int, input().split()))

S.sort(reverse=True)

if all(S[2**i-1] > S[2**(i+1)-1] for i in range(N)):
    print("Yes")
else:
    print("No")