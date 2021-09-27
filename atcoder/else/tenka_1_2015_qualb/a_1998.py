A = [100, 100, 200]

while len(A) < 20:
    A.append(A[-3] + A[-2] + A[-1])

print(A[19])
