X = int(input())

money = 100
for i in range(4000):
    if money >= X:
        print(i)
        break
    money = (money * 101) // 100