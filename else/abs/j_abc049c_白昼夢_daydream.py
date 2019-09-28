import sys
sys.setrecursionlimit(10**8)

S = input()
len_S = len(S)

words = ["dream", "dreamer", "erase", "eraser"]

memo = [None]*(len_S+10)
def f(i):
    if i == 0:
        return True
    if memo[i] == None:
        memo[i] = False
        for word in words:
            if word == S[i-len(word):i] and f(i-len(word)):
                memo[i] = True
    return memo[i]

print("YES" if f(len_S) else "NO")


    

################################

# import re

# S = input()

# if re.match("^(dream|dreamer|erase|eraser)*$", S):
#     print("YES")
# else:
#     print("NO")