A, B, C, D = map(int, input().split())

is_prime = [1]*200
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, 200):
    if not is_prime[i]:
        continue
    for j in range(i+i, 200, i):
        is_prime[j] = 0

# C~Dのどの数を足しても素数にならないようにする

for x in range(A, B+1):
    if all(not is_prime[x+y] for y in range(C, D+1)):
        print("Takahashi")
        exit()
print("Aoki")
