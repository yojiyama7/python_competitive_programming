# 20210123 100%
# 日付と理解度をメモ

# dp においては 1-indexed の方が便利?
# dp[i] の i が 現実の数とリンクすること(?)がおおいため, i = 0 を初期値(?)にしたいため
### i 個の時の, i 番目までの という意味

# とりあえず 入力, dp配列共に 1-indexed で持つことにする ( 0-indexed | 1-indexed )
# もらうdpで書いてみる ( もらう | 配る )
# for文を基本形に、再帰の方がやりやすいところは再帰で ( for文 | 再帰 )
# 定数にできるところはしてもいいかも index の最大値がわかる時など


INF = float("inf")

N = int(input())
H = list(map(int, input().split()))

H = [None] + H

dp = [INF for _ in range(N+1)]
dp[1] = 0
for i in range(2, N+1):
	if i - 2 >= 1:
		dp[i] = min(
			dp[i-1] + abs(H[i] - H[i-1]),
			dp[i-2] + abs(H[i] - H[i-2]),
		)
	else:
		dp[i] = dp[i-1] + abs(H[i] - H[i-1])

print(dp[N])
