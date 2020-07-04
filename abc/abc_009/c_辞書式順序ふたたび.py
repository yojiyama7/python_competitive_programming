# 何言ってるか 分からなみ が深い

# やはりあんま何言ってるかわからん。(2019/07/03)
# from collections import Counter

from collections import Counter

N, K = map(int, input().split())
S = input()

remain_chars = sorted(S)

t = ""
diff = 0
for i in range(N):
    for c in remain_chars:
        diff1 = s[i] != c
        counter = Counter(S[i+1:]+c) - Counter(remain_chars)
        diff2 = sum(counter.values())
        if diff + diff1 + diff2 <= K:
            ans += c
            ss.remove(c)
            diff += diff1
            break