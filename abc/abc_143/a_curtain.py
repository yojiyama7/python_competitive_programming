A, B = map(int, input().split())

print(max(0, A-2*B))
# ↑等しい↓
print(0 if A-2*B < 0 else A-2*B)
