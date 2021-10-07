A, B = map(int, input().split())

def f(x):
    return x//4 - x//100 + x//400

ans = f(B) - f(A-1)
print(ans)