N = int(input())
A = list(map(int, input().split()))

# コピペ
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

bit = Bit(300001)
score = 0
for i, a in enumerate(A):
    a = a+1
    bit.add(a, 1)
    score += i + 1 - bit.sum(a)

print(score)