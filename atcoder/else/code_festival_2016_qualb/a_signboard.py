S = input()

correct = "CODEFESTIVAL2016"

ans = sum(a != b for a, b in zip(correct, S))
print(ans)
