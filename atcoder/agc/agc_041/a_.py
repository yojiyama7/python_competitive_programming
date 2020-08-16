# 10 1 8 

# 1, 8
# 1, 7
# 2, 6
# 3, 5
# 4, 4

# 1, 8
# 2, 9
# 3, 10
# 4, 10
# 5, 9
# 6, 8
# 7, 7

N, A, B = map(int, input().split())

def solve(n, a, b):
    m = b-a
    if m%2:
        return min(
            a     + solve(b-a, 1, b-a),
            n-b+1 + solve(n, a+(n-b+1), n),
        )
    else:
        return m//2

print(solve(N, A, B))