N, M = map(int, input().split())
A = [input() for _ in range(2*N)]

def to_num(c):
    return "GCP".find(c)
def janken(a_hand, b_hand):
    x, y = to_num(a_hand), to_num(b_hand)
    return "dba"[(x - y + 3) % 3] 

players = [[i, a, 0] for i, a in enumerate(A)]
sort_key = (lambda x: (-x[2], x[0]))

for i in range(M):
    for j in range(N):
        a, b = players[2*j], players[2*j+1]
        a_hand, b_hand = a[1][i], b[1][i]
        result = janken(a_hand, b_hand)
        if result == 'a':
            a[2] += 1
        elif result == 'b':
            b[2] += 1
    players.sort(key=sort_key)

ans = [p[0]+1 for p in players]

print(*ans, sep='\n')

################################

# N, M = map(int, input().split())
# A = [input() for _ in range(2*N)]

# def to_num(c):
#     return "GCP".find(c)
# def janken(a, b):
#     if a == b:
#         return "draw"
#     elif (a+1)%3 == b:
#         return "win"
#     else:
#         return "lose"

# A_num = [list(map(to_num, a)) for a in A]

# score = [0]*(2*N)

# players = list(range(2*N))
# for i in range(M):
#     players.sort(key=lambda x: (-score[x], x))
#     for j in range(len(players)//2):
#         a = players[2*j]
#         b = players[2*j+1]
#         a_hand = A_num[a][i]
#         b_hand = A_num[b][i]
#         res = janken(a_hand, b_hand)
#         if res == "win":
#             score[a] += 1
#         elif res == "lose":
#             score[b] += 1

# players.sort(key=lambda x: (-score[x], x))
# ans = [p+1 for p in players]
# print(*ans, sep='\n')
