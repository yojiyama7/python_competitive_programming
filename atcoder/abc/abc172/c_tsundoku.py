from itertools import accumulate as acc
from bisect import bisect_right

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_acc = [0] + list(acc(A))
B_acc = [0] + list(acc(B))

max_num = 0
for i in range(min(K+1, N+1)):
    # Aからi冊読む
    count_a = i
    time = A_acc[i]
    
    # Bから読めるだけ読む
    count_b = bisect_right(B_acc, K-time)-1
    time += B_acc[count_b]
    
    # print(time, count_a, count_b)
    count = count_a + count_b
    if time <= K:
        max_num = max(max_num, count)

print(max_num)

################################

# N, M, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# A.reverse()
# B.reverse()

# books = []
# for i in range(N+M):
#     if A and B :
#         if A[-1] <= B[-1]:
#             books.append(A.pop())
#         else:
#             books.append(B.pop())
#     elif A:
#         books.append(A.pop())
#     else:
#         books.append(B.pop())

# books.reverse()
# # print(books)

# time = 0
# c = 0
# for _ in range(N+M):
#     if time + books[-1] <= K:
#         time += books.pop()
#         c += 1
#     else:
#         break

# print(c)