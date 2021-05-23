S = input()

if set(S[::2])-set("RUD") == set(S[1::2])-set("LUD") == set():
    print("Yes")
else:
    print("No")