S = input()
T = input()
S_len = len(S)
T_len = len(T)

S = "_" + S
# 20210123 40%

T = "_" + T

# dp[i][j]: S[:i], T[:j] での LCS(Longest Common Subsequence)最長共通部分列 の長さ
dp = [[0 for _ in range(T_len+1)] for _ in range(S_len+1)]
for i in range(1, S_len+1):
	for j in range(1, T_len+1):
		if S[i] == T[j]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(
				dp[i-1][j],
				dp[i][j-1],
			)

# 復元(LCS, dpの値を利用して逆算)
# print(dp[S_len][T_len])
ans_len = dp[S_len][T_len]
ans_array = ["_"]*(ans_len+1)
i = S_len
j = T_len
while ans_len > 0:
	# print(i,j,S,T)
	if S[i] == T[j]:
		ans_array[ans_len] = S[i]
		ans_len -= 1
		i -= 1
		j -= 1
	# (i, j) から (i-1, j) か (i, j-1) に戻りたい
	# S[i] != T[i] よりどちらも使わないのでdpの値が変わらない(長さの帳尻があう)方向に戻る
	elif dp[i-1][j] == dp[i][j]:
		i -= 1
	else:
		j -= 1

ans = "".join(ans_array[1:])
print(ans)
