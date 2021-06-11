S = input()

ans = sum(S[i:i+4] == "ZONe" for i in range(12-4+1))
print(ans)