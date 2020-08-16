N, K = map(int, input().split())

# x個の選んだ際の合計値の最小 から 最大 の間の数すべてがx個選んだ際の合計値になりうると仮定

def one_to_a_sum(a):
    return (a+1)*a//2

def a_to_b_sum(a, b):
    return one_to_a_sum(b) - one_to_a_sum(a-1)

sum_num = 0
for i in range(K, N+2):
    min_num = a_to_b_sum(0, i-1)
    max_num = a_to_b_sum(N-(i-1), N)
    sum_num = (sum_num + max_num-min_num+1) % (10**9+7)

print(sum_num)
