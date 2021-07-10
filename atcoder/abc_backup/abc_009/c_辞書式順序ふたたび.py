# 何言ってるか 分からなみ が深い

# やはりあんま何言ってるかわからん。(2019/07/03)
# from collections import Counter

<<<<<<< HEAD
# 20200704
=======
>>>>>>> 1cecfc02f2e087e5e3a9ea921d09cab580c84bb3
from collections import Counter

N, K = map(int, input().split())
S = input()

<<<<<<< HEAD
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
=======
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
>>>>>>> 1cecfc02f2e087e5e3a9ea921d09cab580c84bb3
