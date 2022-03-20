N = int(input())
T = input()

if T == "1":
    print(2 * 10**10)
    exit()

cnt = None
part = "110"
for i in range(3):
    # print(i, T[:i], part[::-1][:i][::-1])
    if T[:i] != part[::-1][:i][::-1]:
        continue
    if any(t != part[j%3] for j, t in enumerate(T[i:])):
        continue
    cnt = (i > 0) + -(-(N-i)//3)

if cnt == None:
    print(0)
else:
    ans = 10**10 - cnt + 1
    print(ans)
