from itertools import chain

l = [[] for _ in range(11)]
l[0] = list(map(str, range(1, 10)))
for i in range(10):
    for x in l[i]:
        last = int(x[-1])
        for m in {max(0, last-1), last, min(9 ,last+1)}:
            m = str(m)
            l[i+1].append(x+m)

q = list(map(int, chain(*l)))
q.sort()
# print(len(q))
K = int(input())

print(q[K-1])

# l = []
# i = 0
# while len(l) < 100:
#     nums = list(map(int, str(i)))
#     if all(abs(nums[j]-nums[j+1]) <= 1 for j in range(len(nums)-1)):
#         l.append(i)
#     i += 1
# print(l)