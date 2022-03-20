S = input()
T = input()

if S == T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    x = S[:i] + S[i+1] + S[i] + S[i+2:]
    if x == T:
        print("Yes")
        exit()
print("No")