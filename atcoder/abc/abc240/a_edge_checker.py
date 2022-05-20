A, B = map(int, input().split())

if (A-B)%10 in [1, 9]:
    print("Yes")
else:
    print("No")