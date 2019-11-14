N = int(input())

def ceil(x):
    return int(-(-x//1))

for i in range(ceil(N**(1/2)), 0, -1):
    if N%i == 0:
        print(i+N//i-2)
        exit()