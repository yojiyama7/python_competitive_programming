S = input()

if set(S) - set(map(str, range(10))) == set():
    print(int(S)*2)
else:
    print("error")

