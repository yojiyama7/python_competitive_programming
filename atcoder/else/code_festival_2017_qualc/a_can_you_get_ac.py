S = input()

if any([S[i:i+2] == "AC" for i in range(len(S)-1)]):
    print("Yes")
else:
    print("No")