S = input()

n = len(S)
print(sum([a != b for a, b in zip(S[:n//2], S[::-1][:n//2])]))