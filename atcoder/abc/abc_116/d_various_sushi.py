# ヒープ以降をどう実装するかわからんな
# キレそう。heap in heap とか？ 考えてからコード書いた方が良さげ

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


class Heap:
    def __init__(self, nums=[]):
        self.is_used = False
        self.size = 0
        self.nums = []
        for num in nums:
            self.insert(num)

    def insert(self, num):
        self.nums.append(num)
        self.size += 1

        i = self.size-1
        while not (i == 0 or self.nums[i] < self.nums[(i-1)//2]):
            swap(self.nums, i, (i-1)//2)
            i = (i-1)//2

    def __repr__(self):
        return f'<{" ".join(map(str, self.nums))}>'

    def get_root(self):
        return self.nums[0]

    def pop_root(self):
        print(f"size: {self.size}")
        if self.size == 0:
            return False
        root = self.nums[0]
        v = self.nums.pop()
        self.size -= 1
        if self.size == 0:
            return root

        i = 0
        while i*2+1 < self.size:
            c1, c2 = i*2+1, i*2+2
            if c2 < self.size and self.nums[c2] > self.nums[c1]:
                c1 = c2
            if self.nums[c1] <= v:
                break
            self.nums[i] = self.nums[c1]
            i = c1
        self.nums[i] = v
        return root
    
    def __lt__(self, other):
        return self.get_root() < other.get_root()
    def __le__(self, other):
        return self.get_root() <= other.get_root()
    def __eq__(self, other):
        return self.get_root() == other.get_root()
    def __ne__(self, other):
        return self.get_root() != other.get_root()
    def __gt__(self, other):
        return self.get_root() > other.get_root()
    def __ge__(self, other):
        return self.get_root() >= other.get_root()


# l = list(range(32, -1, -1))[::-1]
# h = Heap(l)
# # print(h)
# # print(h.pop_root())
# # print(h)
# for i in range(h.size):
#     print(h.pop_root())

N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]

e = [Heap() for _ in range(N+1)]
for t, d in TD:
    e[t].insert(d)
hq = Heap(e)

added_hq = Heap()
score = 0
for i in range(K):
    r = hq.pop_root()
    score += r.pop_root()