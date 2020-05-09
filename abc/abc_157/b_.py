A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

l = [[(a_i in B) for a_i in a] for a in A]

x = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

flag = any(all(l[y][x] for x, y in pos_l) for pos_l in x)
# print(l)

# flag = 0
# for y in range(3):
#     flag |= all(l[y])

# for x in range(3):
#     flag |= all([l[x][y] for y in range(3)])

# flag |= all([l[y][x] for x, y in [(0, 0), (1, 1), (2, 2)]])

# flag |= all([l[y][x] for x, y in [(0, 2), (1, 1), (2, 0)]])

print("Yes" if flag else "No")