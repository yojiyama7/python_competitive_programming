N = int(input())

s, e = 0, N
print(s)
s_num = int(input())
while True:
    mid = (s + e) // 2
    print(mid, flush=True)
    a = int(input())
    is_right = s_num + (mid - s)
    if is_right:
        e = mid
    else:
        s = mid