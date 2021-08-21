### 1. 入力、出力

# S = input()
# print(S)
# print(S[::-1])

### 2. 代入、単純な四則演算処理（+, -, *, /, = など）

# N = 24
# M = 7

# print(N+M, N-M)
# print(N*M, N/M)

# # //, %
# print(N//M, N%M)

# # **
# print(N**M)

# # 演算と同時に代入 (+= など)
# x = N
# print(x)
# x %= 10
# print(x)

### 3. 条件分岐（if 文など）

# age = 19

# if age >= 100:
#     print("too old")

# if age >= 20:
#     print("Yes")
# else:
#     print("No")

# if age < 18:
#     print("child")
# elif age < 20:
#     print("non alcohol")
# else:
#     print("alcohol")

### 4. 繰り返し処理（for 文など）

# # n番目のフィボナッチ数を return する関数 (高速でない)
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# for i in range(12):
#     print(i, fib(i))

# x = 100
# t = ""
# while x != 0:
#     r = x % 2
#     t += str(r)
#     x //= 2
# ans = t[::-1]
# print(x, ans)

### 5. 文字列（string）

# S = input() # <- ComPetItiVe_ProGraMmiNg

# print(type(S), S)

# print(S[4])
# print(S[2:])
# print(S[:8])
# print(S[::3])
# print(S[3:15:3])

### 6. 浮動小数点（double 型など）

# # python では float と呼ばれる 1種類のみ

# x = 3.14
# print(type(x), x)

# x = 10/5
# print(type(x), x)
# x = 10//5
# print(type(x), x)

# x = 1 + 0.3
# print(type(x), x)

### 7. 配列（二次元配列も含む）

# A = [5, 3, 2, 5, 7]

# print(type(A), A, len(A))

# print(A[0])
# print(A[1:3]) # 半開区間: 1以上3未満

# A.append(10)
# print(A, len(A))

# A.pop()
# print(A)
# A.pop()
# print(A)

# B = [[1, 2, 3], [4, 5, 6, 7]]

# print(B)

