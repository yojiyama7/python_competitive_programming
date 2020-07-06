# 何言ってるか 分からなみ が深い

# やはりあんま何言ってるかわからん。(2019/07/03)
# from collections import Counter

# 20200704
from collections import Counter

N, K = map(int, input().split())
S = input()

remain = sorted(S)
diff = 0
t = ""

for i in range(N):
    for c in remain:
        diff1 = (c != S[i])
        diff2 = sum((Counter(remain) - Counter(c) - Counter(S[i+1:])).values())
        
        # 必ずこのif文でfor文を抜ける
        if diff1 + diff2 + diff <= K:
            remain.remove(c)
            diff += diff1
            t += c
            break

print(t)