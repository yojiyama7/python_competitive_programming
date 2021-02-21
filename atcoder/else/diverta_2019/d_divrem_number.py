N = int(input())

# l = [i for i in range(1, N+1) if N%i == N//i]
# print(l, sum(l))

# 一旦集合にいれたほうがよさげ or i**2 == N の時の例外を考えれれば良さげ
s = {1, N}
for i in range(2, N+1):
    if i**2 > N:
        break
    if N%i == 0:
        s.add(i)
        s.add(N//i)

sum_num = 0
for r in s:
    m = (N//r)-1
    if r < m:
        sum_num += m

print(sum_num)