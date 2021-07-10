S = input()

print(["Sunny", "Cloudy", "Rainy"][("SCR".find(S[0])+1)%3])