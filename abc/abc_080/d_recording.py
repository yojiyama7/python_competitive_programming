from itertools import accumulate

N, C = map(int, input().split())
STC = [list(map(int, input().split())) for _ in range(N)]

channels = [[0]*(10**5+1) for _ in range(C)]
for s, t, c in STC:
    # print((s, t))
    s, t, c = s-1, t-1, c-1
    channels[c][s] += 1
    channels[c][t] -= 1
all_channels = [0]*(10**5+1)
for channel in channels:
    # print(channel)
    for j, x in enumerate(channel):
        if x == 1:
            all_channels[j] += 1
        if x == -1:
            all_channels[j+1] -= 1 


a = list(accumulate(all_channels))
# print(a)

print(max(a))