class LazySegTree_RUQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v
    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def query(self,l,r):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

INF = 10**18

W, N = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]

st = LazySegTree_RUQ([0]*W, max, -INF)
for l, r in LR:
    l -= 1
    max_h = st.query(l, r)
    print(max_h+1)
    st.update(l, r, max_h+1)

################################

# W, N = map(int, input().split())
# LR = [list(map(int, input().split())) for _ in range(N)]

# def sqrt_roundup(x):
#     ok, ng = x, 0
#     while abs(ok-ng) > 1:
#         mid = (ok+ng)//2
#         if mid**2 >= x:
#             ok = mid
#         else:
#             ng = mid
#     return ok

# class SquareDivision:
#     def __init__(self, n):
#         self.n = n
#         self.n_sqrt = sqrt_roundup(n)
#         # print(n, self.n_sqrt)
#         self.data = [0]*n
#         self.set_bucket = [0]*self.n_sqrt
#         self.bucket = [0]*self.n_sqrt

#     def to_bucket_id(self, i):
#         return i//self.n_sqrt

#     def set_point(self, i, v):
#         self.data[i] = v
#         bi = self.to_bucket_id(i)
#         self.bucket[bi] = max(v, self.bucket[bi])

#     def set_range(self, i, j, v):
#         ba, bb = -(-i//self.n_sqrt), j//self.n_sqrt
#         a, b = ba*self.n_sqrt, bb*self.n_sqrt
#         for x in range(i, a):
#             self.set_point(x, v)
#         for bx in range(ba, bb):
#             self.set_bucket[bx] = v
#             self.bucket[bx] = v
#         for x in range(b, j):
#             self.set_point(x, v)
        
#     def get_point(self, i):
#         bi = self.to_bucket_id(i)
#         if self.set_bucket[bi] > self.data[i]:
#             self.data[i] = self.set_bucket[bi]
#         return self.data[i]
    
#     def get_range(self, i, j):
#         ba, bb = -(-i//self.n_sqrt), j//self.n_sqrt
#         a, b = ba*self.n_sqrt, bb*self.n_sqrt
#         # print(i, a, (ba, bb), b, j)
#         ans = 0
#         for x in range(i, a):
#             ans = max(ans, self.get_point(x))
#         for bx in range(ba, bb):
#             ans = max(ans, self.bucket[bx])
#         for x in range(b, j):
#             ans = max(ans, self.get_point(x))
#         return ans

# sd = SquareDivision(W)
# for l, r in LR:
#     l -= 1
#     max_h = sd.get_range(l, r)
#     print(max_h+1)
#     sd.set_range(l, r, max_h+1)
#     # print((l, r), max_h+1)
#     # print(sd.bucket)
#     # print(sd.data)

