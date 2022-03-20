# BC を D と置き換える -> ある操作の前後で変わらないもの、共通のものを考える
# D..DA..A の形にするときの swap 回数を考える

# swap と 転倒数 の 関係

from itertools import chain

# D < A として 転倒数を求める
def inv_num(l):
    cnt = 0
    a_cnt = 0
    for l_i in l:
        if l_i == "A":
            a_cnt += 1
        else:
            cnt += a_cnt
    return (cnt)

S = input()

S_len = len(S)

t = S.replace("BC", "D")

q = list(chain(*[t_i.split("B") for t_i in t.split("C")]))

q.sort(reverse=True)
# print(q)
while q and q[-1] == "":
    q.pop()

print(sum(map(inv_num, q)))

################################

# S = input()

# S_len = len(S)

# cnt = 0
# b_is_abc = 0
# i = 0
# while i < S_len:
#     # print(i)
#     a = 0
#     while i < S_len and S[i] == "A":
#         a += 1
#         i += 1
#     bc = 0
#     while i < S_len and S[i:i+2] == "BC":
#         bc += 1
#         i += 2
#     while i < S_len and S[i] != "A" and S[i:i+2] != "BC":
#         i += 1
#     # print(i, a, bc)
#     if a >= 1 and bc >= 1:
#         p = a+bc-1
#         cnt += 
#         cnt += b_is_abc
#         b_is_abc += 1
#     else:
#         b_is_abc = 0
#     # print(cnt)

# print(cnt)