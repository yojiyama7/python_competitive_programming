a, b, x = [int(m) for m in input().split(" ")]

print("YES" if 0 <= x-a and x <= a+b else "NO")