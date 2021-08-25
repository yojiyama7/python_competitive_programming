N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if i*j == N:
            print("Yes")
            exit()
print("No")

################################

# N = int(input())

# def f():
#     for i in range(1, int(N**(1/2))+2):
#         if N%i == 0 and all(1 <= x <= 9 for x in [i, N//i]):
#             return "Yes"
#     return "No"

# print(f())