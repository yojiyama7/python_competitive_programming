N = int(input())

t = ""
while N > 0:
    t += chr((N-1)%26 + 97)
    N = (N-1)//26

print(t[::-1])