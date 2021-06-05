# https://atcoder.jp/contests/abc122/tasks/abc122_b

S = input()

ans = 0
for i in range(len(S)+1):
	for j in range(i, len(S)+1):
		if all(c in "ACGT" for c in S[i:j]):
			ans = max(ans, j - i)

print(ans)
