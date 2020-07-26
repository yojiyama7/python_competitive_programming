# A**5 = X + B**5
X = int(input())

l = []
for i in range(-300, 300):
    l.append(i**5)

for b, b_5 in enumerate(l, start=-300):
    # print(b, b_5, X)
    if X+b_5 in l:
        a_5 = X+b_5
        a = l.index(a_5)-300
        print(a, b)
        break