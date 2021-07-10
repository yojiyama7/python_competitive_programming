N = int(input())
B = list(map(int, input().split()))

a_list = [10**18]*N
for i, b in enumerate(B):
    a_list[i] = min(a_list[i], b)
    a_list[i+1] = min(a_list[i+1], b)

print(sum(a_list))