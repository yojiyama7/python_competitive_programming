X = int(input())

sum_num = (X//500)*1000
X %= 500
sum_num += (X//5)*5

print(sum_num)