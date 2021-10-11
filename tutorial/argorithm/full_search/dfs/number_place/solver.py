import sys
sys.setrecursionlimit(10**8)

EMPTY_CHAR = '.'

def str_to_line(s):
    res = [0 if c == EMPTY_CHAR else int(c) for c in s]
    return res

def str_list_to_matrix(strs):
    res = [str_to_line(s) for s in strs]
    return res                               

to_matrix = str_list_to_matrix

def to_str_list(matrix):
    res = []
    for row in matrix:
        t = ''.join(EMPTY_CHAR if v == 0 else str(v) for v in row)
        res.append(t)
    return res

class NumberPlaceSolver:
    def __init__(self, matrix):
        self.rows = [set() for _ in range(9)]
        self.columns = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        self.matrix = [[0 for _ in range(9)] for _ in range(9)]
        for y, row in enumerate(matrix):
            for x, v in enumerate(row):
                self.place(x, y, v)

    def to_box_idx(self, x, y):
        bx, by = x//3, y//3
        res = 3*by + bx
        return res

    def place(self, x, y, v):
        self.matrix[y][x] = v
        self.rows[y].add(v)
        self.columns[x].add(v)
        self.boxes[self.to_box_idx(x, y)].add(v)

    def remove(self, x, y):
        v = self.matrix[y][x]
        self.rows[y].remove(v)
        self.columns[x].remove(v)
        self.boxes[self.to_box_idx(x, y)].remove(v)
        self.matrix[y][x] = 0
    
    def is_valid(self, x, y, v):
        if v in self.rows[y]:
            return False
        if v in self.columns[x]:
            return False 
        if v in self.boxes[self.to_box_idx(x, y)]:
            return False
        return True

    def solve(self, idx=0):
        if idx == 81:
            ans = [row[:] for row in self.matrix]
            return [ans]
        x, y = idx//9, idx%9
        if self.matrix[y][x]:
            return self.solve(idx+1)
        ans_list = []
        for i in range(1, 10):
            if not self.is_valid(x, y, i):
                continue
            self.place(x, y, i)
            ans_list += self.solve(idx+1)
            self.remove(x, y)
        return ans_list

    def print(self, matrix=None):
        if matrix == None:
            matrix = self.matrix
        strs = to_str_list(matrix)
        print(*strs, sep='\n')

S = [input() for _ in range(9)]

matrix = to_matrix(S)
solver = NumberPlaceSolver(matrix)
ans_list = solver.solve()

# 適当に書いています
for n, ans in enumerate(ans_list, start=1):
    print(f"No.{n:0>3}")
    print(*to_str_list(ans), sep='\n')
    print()
