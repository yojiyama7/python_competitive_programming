S = input()
T = input()

n, m = len(S), len(T)

min_num = 10**18
for i in range(n-m+1):
    # print(S[i:i+m], T)
    x = sum(a != b for a, b in zip(S[i:i+m], T))
    min_num = min(min_num, x)

print(min_num)