H, W = map(int, input().split())
S = [input().split() for _ in range(H)]

chars = [chr(ord('A') + i) for i in range(26)]

for i, s in enumerate(S):
    for j, c in enumerate(s):
        if c == "snuke":
            print(chars[j] + str(i+1))