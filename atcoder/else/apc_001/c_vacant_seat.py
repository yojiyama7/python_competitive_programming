# インタラクティブおもろい

N = int(input())

print(0)

s_num = ["Male", "Female", "Vacant"].index(input())
if s_num == 2:
    exit()
    
ok, ng = 0, N
while True:
    mid = (ok + ng) // 2
    print(mid, flush=True)
    a = ["Male", "Female", "Vacant"].index(input())
    if a == 2:
        exit()
    is_right = (a == (s_num + (mid - ok)) % 2)
    if is_right:
        ok = mid
        s_num = a
    else:
        ng = mid
