from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

if Counter(T) - Counter(D) == Counter([]):
    print("YES")
else:
    print("NO")