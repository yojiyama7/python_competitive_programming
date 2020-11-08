ABCDE = [int(input()) for _ in range(5)]
K = int(input())

if max(ABCDE) - min(ABCDE) > K:
    print(":(")
else:
    print("Yay!")