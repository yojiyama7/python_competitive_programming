S, P = map(int, input().split())

for n in range(1, int(P**0.5)+2):
    if P%n == 0 and n+P//n == S:
        print("Yes")
        exit()
print("No")
