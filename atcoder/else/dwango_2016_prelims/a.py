# 解説みて　こんなバカなことあるかと思いました
# 25の倍数にすべて包括されてるやんけ

N = int(input())

print(N//25)

################################

# # NON SUBMITED

# INF = 10**18

# N = int(input())

# s = set()
# for i in range(1, int(N**0.5)+2):
#     if N%i == 0:
#         s.add(i)
#         s.add(N//i)

# niconico = set()
# for i in range(1, INF):
#     x = int("25"*i)
#     if x > N:
#         break
#     niconico.add(x)

# print(s, niconico)

# ans = len(s & niconico)
# print(ans)