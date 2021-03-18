# 1-indexed 閉区間 add_point sum_range
class Bit:
    def __init__(self, n):
        self.n = n
        self.array = [0]*(n+1)
    
    def add(self, x, w=1):
        # print(f"{id(self)}: Bit.add({x}, {w})")
        while (x <= self.n):
            self.array[x] += w
            x += (x & -x)
    
    def sum(self, x, y=None):
        # print(f"{id(self)}: Bit.sum({x}, {y})")
        if y == None:
            # 1~x
            sum_num = 0
            while (x > 0):
                sum_num += self.array[x]
                x -= (x & -x)
            return sum_num
        else:
            # x~y
            return self.sum(y) - self.sum(x-1)

# 1-indexed 閉区間 add_range sum_point
class Bit:
    def __init__(self, n):
        self.n = n
        self.array = [0]*(n+1)
    
    def add(self, x, w=1):
        # print(f"{id(self)}: Bit.add({x}, {w})")
        while (x <= self.n):
            self.array[x] += w
            x += (x & -x)
    
    def sum(self, x, y=None):
        # print(f"{id(self)}: Bit.sum({x}, {y})")
        if y == None:
            # 1~x
            sum_num = 0
            while (x > 0):
                sum_num += self.array[x]
                x -= (x & -x)
            return sum_num
        else:
            # x~y
            return self.sum(y) - self.sum(x-1)


if __name__ == "__main__":
    # JUDGE: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=jp

    N, Q = list(map(int, input().split()))
    CXY = [list(map(int, input().split())) for _ in range(Q)]

    bit = Bit(100000)

    for c, x, y in CXY:
        if c == 0:
            bit.add(x, y)
        else:
            print(bit.sum(x, y))
    
    ################################

    # bit = Bit(0)
    # print(bit.sum(0))
    
    # bit = Bit(1)
    # bit.add(1)
    # print(bit.sum(0))
    # print(bit.sum(1))
    # bit.add(1, 10)
    # print(bit.sum(1))
    # bit.add(1, -10)
    # print(bit.sum(1))

    # bit = Bit(2)
    # bit.add(1, 7)
    # bit.add(2, 10)
    # print(bit.sum(1))
    # print(bit.sum(2))

    # bit = Bit(10)
    # [bit.add(i, i) for i in range(1, 11)]
    # print(bit.sum(10))

    # bit = Bit(127)
    # bit = Bit(128)
    # bit = Bit(129)
    # bit = Bit(10000)
    
    # bit = Bit(1000000)
    # [bit.add(i, i) for i in range(1, 1000001)]
    # print(bit.sum(1000000))