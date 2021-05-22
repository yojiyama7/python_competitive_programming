S = input()

ans = S.replace('6', 'z').replace('9', '6').replace('z', '9')
ans = ans[::-1]

print(ans)