S = input()

l = []
t = ""
for i, s in enumerate(S):
    if s == "x":
        continue
    t += s
    l.append(i)

if t != t[::-1]:
    print(-1)
    exit()

l = [-1] + l + [len(S)]
q = [l[i+1] - l[i] - 1 for i in range(len(l)-1)]
# print(q)
cost = 0
for i in range(len(q)//2):
    cost += abs(q[i] - q[-(i+1)])

print(cost)
