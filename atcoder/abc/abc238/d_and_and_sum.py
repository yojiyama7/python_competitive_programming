T = int(input())

# def b(x):
#     s = bin(x)[2:]
#     return f"{s:0>10}"

for _ in range(T):
    A, S = map(int, input().split())
    if A*2 > S:
        print("No")
        continue
    remain = S - A*2
    # print(b(A))
    # print(b(S))
    # print(b(remain))
    if remain&A:
        print("No")
    else:
        print("Yes")
