N, M = map(int, input().split())

# Mを i*j 
# j がN以上なら i は a の 公約数である
# i がN以上なら j は a の 公約数である
# 最大値を記録しながら、公約数を全て探索(i, j を共に記録)
max_num = 1
for i in range(1, int(M**(1/2))+2):
    if M%i:
        continue
    j = M // i
    if j >= N:
        max_num = max(max_num, i)
    if i >= N:
        max_num = max(max_num, j)

print(max_num)