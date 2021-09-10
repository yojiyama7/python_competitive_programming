S = input()

if all(S[i:i+2] == "hi" for i in range(0, len(S), 2)):
    print("Yes")
else:
    print("No")