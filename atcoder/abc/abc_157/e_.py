################################

# # セグ木不完全理解者

# # UNFINISHED

# def char_to_num(c):
#     x = ord(c)-97
#     return (1<<x)

# def to_power_of_two(n):
#     if (n & (n-1)) == 0:
#         return n
#     return 1<<(len(bin(n))-2)

# def num_from(bit_n):
#     return bin(bit_n)[2:].count("1")

# # print(to_power_of_two(8))

# # 1-indexed
# class SegmentTree:
#     def __init__(self, l):
#         self.n = to_power_of_two(len(l))
#         self.l = [0]*(2*self.n)
#         for i, l_i in enumerate(l):
#             self.l[self.n+i] = l_i
#         self.c_ = 0
    
#     def update(self, i, v):
#         x = self.n+i
#         self.l[x] = v
#         while x > 0:
#             x = x//2
#             self.l[x] = self.l[2*x] | self.l[2+x]
            
    
#     def find(self, i, j, a=1, b="self.n"):
#         if b == "self.n":
#             b = self.n+1
#         # print(i, j, [a, b])
#         # if self.c_ < 10:
#         #     print(i, j, a, b)
#         #     self.c_ += 1
#         if abs(a-b) == 1:
#             return self.l[self.n-1+a]
#         elif i <= a and b <= j:
#             w = abs(a-b)
#             x = self.n//w + a//w
#             print(a, b, x, [self.n//w, a//w])
#             return self.l[x]
#         elif b <= i or j <= a:
#             return 0
#         else:
#             x = self.find(i, j, a, (a+b-1)//2+1)
#             y = self.find(i, j, (a+b-1)//2+1, b)
#             return x | y

# N = int(input())
# S = input()
# Q = int(input())
# QUERY = [input().split() for _ in range(Q)]

# segtree = SegmentTree(list(map(char_to_num, S)))

# for t, *query in QUERY:
#     t = int(t)
#     if t == 1:
#         i, c = query
#         i, c = int(i), c
#         segtree.update(i, char_to_num(c))
#     elif t == 2:
#         i, j = map(int, query)
#         i, j = i, j+1
#         x = num_from(segtree.find(i, j))
#         print(x)