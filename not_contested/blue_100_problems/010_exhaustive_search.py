# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

s = {0}
for a in A:
	s |= {s_i+a for s_i in s}

for m in M:
	print("yes" if m in s else "no")
