S = input()

S_len = len(S)

for i in range(S_len+1):
    for j in range(i, S_len+1):
        if S[:i] + S[j:] == "keyence":
            print("YES")
            exit()
print("NO")