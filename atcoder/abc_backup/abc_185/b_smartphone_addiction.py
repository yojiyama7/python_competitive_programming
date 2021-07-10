N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

def is_able():
    before = 0
    battery = N
    for a, b in AB:
        battery -= a - before
        if battery <= 0:
            return False
        battery = min(battery + b-a, N)
        before = b
    battery -= T - before
    if battery <= 0:
        return False
    return True

print("Yes" if is_able() else "No")
