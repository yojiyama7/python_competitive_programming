A, B, C, X = [int(input()) for _ in range(4)]

count = 0
for a_i in range(A+1):
    for b_i in range(B+1):
        for c_i in range(C+1):
            if (500*a_i + 100*b_i + 50*c_i) == X:
                count += 1
print(count)