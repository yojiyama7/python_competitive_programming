N = int(input())
A = list(map(int, input().split()))

all_fav_num_xor = 0
for a in A:
    all_fav_num_xor ^= a

l = [all_fav_num_xor ^ a for a in A]

print(*l)