N = 10**9+7

# is_prime
def func(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

print("Yes" if func(N) else "No")
