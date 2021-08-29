N = int(input())

ans = ""
x = N
while x:
    if x%2 == 1:
        ans += "A"
    x //= 2
    ans += "B"

print(ans[::-1])
