N = int(input())

memo = [None]*50
def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if memo[x] == None:
        memo[x] = fib(x-1) + fib(x-2) 
    return memo[x]

print(fib(N+1))
