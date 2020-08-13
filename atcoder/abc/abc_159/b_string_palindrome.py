S = input()

n = len(S)

def is_palindrome(s):
    return s == s[::-1]

if all(map(is_palindrome, [S, S[:n//2], S[n//2+1:]])):
    print("Yes")
else:
    print("No")