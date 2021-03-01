# LCA: lowest common ancestor (2ノード間における、最小の(最も深い位置にある)共通の祖先)

# 任意の頂点の出現回数が偶数の場合成り立つ(1) だとYES
# そうではない場合(奇数回現れる頂点が1つ以上あるの場合) だとNO 
# これらをそれぞれ証明することで (1) が必要十分であると示せる

from itertools import chain
from collections import Counter

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

ans = all(x%2 == 0 for x in Counter(chain(*AB)).values())

print("YES" if ans else "NO")