Istr = input

S = Istr()

smalls = {chr(ord('a') + i) for i in range(26)}
bigs = {chr(ord('A') + i) for i in range(26)}

if set(S[::2]) - smalls | set(S[1::2]) - bigs:
    print("No")
else:
    print("Yes")
