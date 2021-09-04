H1, M1, H2, M2, K = map(int, input().split())

a = H1*60 + M1
b = H2*60 + M2
print(b-a-K)
