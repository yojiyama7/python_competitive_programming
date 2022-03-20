MOD = 998244353

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

# 各辺について考察する
# ある辺を削除した時 各kに対して減るパターン数を考える

# 愚直解: O(2**M * N)
# 考えられるすべてのHについて dfs してkについて数え上げる

# >>> すべての H を考えるのは無理
# 何を全探索するか? -> 各ノードの有無 は 探索可能 (bit 全探索)
# 考えられるHのうち ある頂点集合 で構成されるHについてまとめて数え上げする
# ノード1は固定で必要なので 2~N の最大 16 個

