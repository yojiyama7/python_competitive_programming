from itertools import permutations as permu

ans = 0
for l in permu(range(1, 7)):
    if all(l[i] + l[i+1] != 7 for i in range(5)):
        ans = max(ans, int(''.join(map(str, l))))

print(ans)