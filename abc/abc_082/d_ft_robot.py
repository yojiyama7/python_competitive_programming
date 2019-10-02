# うーんdp、、、

# S = input()
# X, Y = map(int, input().split())
S = "FT"*4000
X, Y = 0, 0

m = [len(s) for s in S.split("T")]
X -= m[0]
ud = m[1::2]
lr = m[2::2]

# i番目を使った時にj番目に存在できるか
dp1 = [[0]*(8000+1) for _ in range(len(ud)+1)]
dp1[0][0] = 1
for i, ud_i in enumerate(ud, start=1):
    dp1[i]

print(lr, ud, (X, Y))