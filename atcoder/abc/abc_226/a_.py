X = input()

a, b = map(int, X.split('.'))
if b >= 500:
    print(a+1)
else:
    print(a)