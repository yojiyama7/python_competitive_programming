from copy import deepcopy

def f(i):
    i = 777

def g(l):
    l[2] += 1

a = [1000, "GGGCCC", 0]
g(l = a[:])
print(a)
