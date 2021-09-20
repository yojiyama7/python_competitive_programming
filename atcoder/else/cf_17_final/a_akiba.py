S = input()


t = ["KIH", "B", "R", ""]

for i in range(1<<4):
    l = ['A' if (i>>j)&1 else '' for j in range(4)]
    p = ''.join(a+b for a, b in zip(l, t))
    if p == S:
        print("YES")
        exit()
print("NO")