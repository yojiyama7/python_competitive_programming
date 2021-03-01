# 貪欲(?)

MOD = 10**9+7

N = int(input())
S = [input() for _ in range(2)]

score = 0
is_skip = 0
before = -1
for i, (s1, s2) in enumerate(zip(*S)):
    if is_skip:
        is_skip = 0
        continue
    if i == 0:
        if s1 == s2:
            score = 3
            before = 0
        else:
            score = 6
            before = 1
            is_skip = True
        continue
    # print(s1, s2, score)
    if before == 0:
        if s1 == s2:
            score *= 2
            before = 0
        else:
            score *= 2
            before = 1
            is_skip = True
    else:
        if s1 == s2:
            score *= 1
            before = 0
        else:
            score *= 3
            before = 1
            is_skip = True
    score %= MOD

print(score)