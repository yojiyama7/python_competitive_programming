ABCD = list(map(int, input().split()))

def solve():
    for i in range(1<<4):
        ab = [0, 0]
        for j in range(4):
            ab[(i>>j)&1] += ABCD[j]
        if len(set(ab)) == 1:
            return "Yes"
    return "No"

print(solve())