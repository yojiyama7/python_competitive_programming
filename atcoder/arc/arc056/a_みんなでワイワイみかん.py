A, B, K, L = map(int, input().split(" "))

print(K//L*B + min(K%L*A, B))