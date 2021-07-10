A, B = map(int, input().split())

print("IMPOSSIBLE" if (A+B)%2 else (A+B)//2)

################################

# A, B = map(int, input().split(" "))

# if abs(A-B)%2 == 0:
#     print(min(A, B) + abs(A-B)//2)
# else:
#     print("IMPOSSIBLE")