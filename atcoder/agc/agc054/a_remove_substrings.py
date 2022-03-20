# できるなら最大でも2回にしかならないところがツボ
# 最大でも一桁通り程度しかない場合にそれぞれについて考える典型
# 内1パターンはelseで処理できるためN-1パターンについての場合分けが考えれればOKというのも典型

N = int(input())
S = input()

if S[0] != S[N-1]:
    print(1)
elif any(S[0] not in [S[1+i], S[1+i+1]] for i in range(N-3)):
    print(2)
else:
    print(-1)