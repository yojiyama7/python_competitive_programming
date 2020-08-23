N = int(input())
S = input()
Q = int(input())
QUERY = [input().split() for _ in range(Q)]
# N = 4
# S = "abcd"
# QUERY = [s.split() for s in [
#     "2 1 4", # 4
#     "2 1 3", # 3
#     "2 3 4", # 2
#     "2 4 4", # 1
#     "1 2 a", # aacd
#     "2 1 2", # 1
#     "2 1 3", # 2
# ]]
# Q = len(QUERY)

def or_more_pow_two(n):
    if (n & (n-1)) == 0:
        return n
    return 1<<(len(bin(n))-2)

class SegmentTree:
    def __init__(self, n, l):
        # たぶん半分のほうがいい
        self.n = or_more_pow_two(n)*2
        self.tree = [0]*self.n
        for i, l_i in enumerate(l):
            self.tree[self.n//2+i] = l_i
        for i in reversed(range(1, self.n//2)):
            self.node_update(i)
            # print(self.tree[i])

    # 1-indexed: [l, r)
    def find(self, l, r, fl=1, fr="self.n//2+1", node=1):
        if fr == "self.n//2+1":
            fr = self.n//2+1
        # print(f"find: ({l}, {r}), ({fl}, {fr}), {node}")
        if l <= fl and fr <= r:
            # print("in", bin(self.tree[node])[2:])
            return self.tree[node]
        elif fr <= l or r <= fl:
            # print("out")
            return 0
        else:
            # print("overlap")
            mid = (fl+fr)//2
            a = self.find(l, r, fl=fl, fr=mid, node=2*node)
            b = self.find(l, r, fl=mid, fr=fr, node=2*node+1)
            return a | b

    def update(self, index, v):
        # print("update:", index, v)
        # ややこしい
        x = self.n//2+index-1
        self.tree[x] = v
        while x > 0:
            x >>= 1
            self.node_update(x)

    def node_update(self, index):
        # print(index, [2*index, 2*index+1], list(map(bin, [self.tree[2*index], self.tree[2*index+1], self.tree[2*index] | self.tree[2*index+1]])))
        self.tree[index] = self.tree[2*index] | self.tree[2*index+1]

def char_to_bit(c):
    i = ord(c) - 97
    return (1 << i)
def bit_to_type_count(b):
    # print(bin(b)[2:])
    r = bin(b)[2:].count("1")
    # print(r)
    return r
# def bit_to_char(b):
#     for i in range(26):


segtree = SegmentTree(N, map(char_to_bit, S))

for t, *query in QUERY:
    t = int(t)
    if t == 1:
        i, c = query
        i, c = int(i), c
        segtree.update(i, char_to_bit(c))
    elif t == 2:
        l, r = map(int, query)
        l, r = l, r+1
        r = segtree.find(l, r)
        r = bit_to_type_count(r)
        print(r)
    # print(list(map(bin, segtree.tree)))

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