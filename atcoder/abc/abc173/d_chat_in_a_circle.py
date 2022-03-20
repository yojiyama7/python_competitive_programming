N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

max_num, *p = A

node_num = N-1

q = [(2*i <= node_num) + (2*i+1 <= node_num) for i in range(1, node_num+1)]

# print(q)
# print(max_1, max_2, sum(p_i*q_i for p_i, q_i in zip(p, q)))
r = max_num + sum(p_i*q_i for p_i, q_i in zip(p, q))
print(r)