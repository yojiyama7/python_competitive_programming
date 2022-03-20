S = [input() for _ in range(4)]

correct = {"H", "2B", "3B", "HR"}
if set(S) == correct:
    print("Yes")
else:
    print("No")
