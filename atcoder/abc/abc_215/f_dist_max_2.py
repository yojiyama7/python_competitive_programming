from bisect import bisect_left, bisect_right

INF = 10**18

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort()
X, Y = zip(*XY)
# print(XY, X, Y)

seg_min = SegTree(Y, min, INF)
seg_max = SegTree(Y, max, -INF)

def is_ok(mid):
    # print("ssssss")
    for x, y in XY:
        l = bisect_right(X, x-mid)
        r = bisect_left(X, x+mid)
        # print(x, y, (x-mid, x+mid), X[l:r])
        if l == 0 and r == N:
            continue
        y_min = min(seg_min.query(0, l), seg_min.query(r, N))
        y_max = min(seg_max.query(0, l), seg_max.query(r, N))
        if abs(y-y_min) >= mid or abs(y-y_max) >= mid:
            # print("eeeeeeee")
            return True
    # print("eeee")
    return False

ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
