N = int(input())
S = input()

ord_A = ord("A")

print("".join([chr((ord(s)-ord_A+N)%26+ord_A) for s in S]))

