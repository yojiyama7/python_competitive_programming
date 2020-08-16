# やはりある程度のfor(繰り返し)で押さえるとこがコツだね。
# そりゃそうなんだけど。 
# あとあんまり 価値/コスト ってのはやらなさそう。
# 純粋な線形探索。

N, H = map(int, input().split(" "))
A, B, C, D, E = map(int, input().split(" "))

min_cost = 10**18
# print(E*N)
for i in range(N+1):
    p = H + (B+E)*i - E*N
    cost = A*i
    j = 0
    if p <= 0:
        j = abs(p)//(D+E)+1
    cost += C*j
    # print(i, j, cost, p)
    min_cost = min(min_cost, cost)

print(min_cost)

################################

# # 毎日E失うとして、各食事をすると満腹度が+E増えるようにする
# # [1]: A円 -> B+E
# # [2]: C円 -> D+E

# # [1]*K, [2]*K, [1]*K+[2], [2]*K+[1] 

# # costの絶対値分の食事をしなくてはならない
# cost = H-E*N

