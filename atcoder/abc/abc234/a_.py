def f(x):
    return x**2 + 2*x + 3

T = int(input())

ans = f(f(f(T) + T) + f(f(T)))

print(ans)