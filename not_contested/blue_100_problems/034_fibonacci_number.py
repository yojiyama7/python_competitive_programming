# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja

N = int(input())

fib = [1, 1]
for i in range(2, N+1):
    fib.append(fib[i-1] + fib[i-2])

print(fib[N])
