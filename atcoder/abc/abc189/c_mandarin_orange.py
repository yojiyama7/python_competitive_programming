# pypy3でO(N^2)は通る 1.5sec ですが
# 制約が絶妙なのは O(N^2*logN) を落とすため

# http://algorithms.blog55.fc2.com/blog-entry-132.html
# O(N) で解けるらしいです復習しろ

INF = float('inf')

N = int(input())
A = list(map(int, input().split()))

max_score = 0
for l in range(N):
    min_num = INF
    for r in range(l, N):
        min_num = min(min_num, A[r])
        # print(l, r, min_num)
        # min 更新と score 更新を同時にやるという頭の良さ
        max_score = max(max_score, min_num*(r-l+1))

print(max_score)