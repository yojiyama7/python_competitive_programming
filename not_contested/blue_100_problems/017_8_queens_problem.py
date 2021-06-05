# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja

K = int(input())
RC = [list(map(int, input().split())) for _ in range(K)]

board = [[0]*8 for _ in range(8)]
rows = [0]*8
columns = [0]*8
rightup_dia = [0]*15
leftup_dia = [0]*15
cnt = 0

for r, c in RC:
	board[r][c] = 1
	rows[r] += 1
	columns[c] += 1
	rightup_dia[r+c] += 1
	leftup_dia[r+(7-c)] += 1
	cnt += 1

def solve(i):
	global cnt
	if i == 64:
		return
	if cnt == 8:
		[print(''.join('.Q'[c] for c in line)) for line in board]
		exit()
	x, y = i%8, i//8
	solve(i+1)
	if rows[y] or columns[x] or rightup_dia[y+x] or leftup_dia[y+(7-x)]:
		return
	board[y][x] = 1
	rows[y] += 1
	columns[x] += 1
	rightup_dia[y+x] += 1
	leftup_dia[y+(7-x)] += 1
	cnt += 1
	solve(i+1)
	board[y][x] = 0
	rows[y] -= 1
	columns[x] -= 1
	rightup_dia[y+x] -= 1
	leftup_dia[y+(7-x)] -= 1
	cnt -= 1

solve(0)
