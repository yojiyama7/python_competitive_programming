from itertools import chain

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

print(sum(chain(*A)) - min(chain(*A))*H*W)