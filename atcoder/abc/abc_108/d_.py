# i と N-i-1 を +1 したり -1 したりするのしんどい
# AC

L = int(input())

N = 20
edges = []
for i in range(N-1):
    edges.append((i, i+1, 0))

ni = 0
while ni < N:
    bi = N-ni-1
    if (L>>bi)&1:
        ni += 1
        break
    ni += 1
while ni < N:
    bi = N-ni-1
    edges.append((ni-1, ni, L>>(bi+1)))
    if (L>>bi)&1:
        edges.append((0, ni, (L>>bi)-1))
    ni += 1

print(N, len(edges))
for e in edges:
    a, b, x = e
    a += 1
    b += 1
    print(a, b, x)

################################

# 詰め甘 わからん
# ? になっている

# L = int(input())

# lbit = None
# for i in range(20):
# 	if L&(1<<i):
# 		lbit = i

# n = lbit+1
# edges = []
# for i in range(lbit):
# 	edges.append([lbit-i-1, lbit-i, 1<<i])
# 	edges.append([lbit-i-1, lbit-i, 0])

# for i in range(lbit):


################################

# # 発想は良かった 50点って感じ

# # 誤読

# L = int(input())

# n = 20
# edge = []
# for i in range(n-1):
# 	edge.append((i, i+1, 0))

# lbit = None
# for i in reversed(range(20)):
# 	# print(i, bin(L>>i))
# 	if (L>>i)&1:
# 		lbit = i
# 		break
# # print(lbit)

# left = 0
# right = 19
# for i in range(lbit):
# 	if (L>>i)&1:
# 		edge.append((right-1, right, 1<<i))
# 		right -= 1
# 	else:
# 		edge.append((left, left+1, 1<<i))
# 		left += 1

# edge.append((0, right, 1<<lbit))

# print(n, len(edge))
# for a, b, cost in edge:
# 	a, b, cost = a+1, b+1, cost
# 	print(a, b, cost)
