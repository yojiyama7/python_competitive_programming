import sys

groups = {
    (1, 3, 5, 7, 8, 10, 12),
    (4, 6, 9, 11),
    (2, )
}

x, y = map(int, input().split(" "))

for group in groups:
    if x in group and y in group:
        print("Yes")
        sys.exit()
print("No")


