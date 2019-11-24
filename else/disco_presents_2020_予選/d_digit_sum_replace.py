# 数学(考察)問題
# ある操作がどのような効果を及ぼすかをいくつかのパターンに分ける
# この問題の場合1回の操作による効果は、
# 1. 各桁の和が変わらず1桁減る
# 2. 桁数が変わらず書く桁の和が9減る
# のどちらかしか無いので、1桁になるまでに (元の桁数 - 1) + ((各桁の和 - 1[この-1を忘れない]) // 9) 回の操作を行うことになる

M = int(input())
DC = [list(map(int, input().split())) for _ in range(M)]

digits_sum = 0
digits_length = 0
for d, c in DC:
    digits_sum += d*c
    digits_length += c

# print(digits_sum, digits_length)

print((digits_length - 1) + ((digits_sum-1) // 9))
