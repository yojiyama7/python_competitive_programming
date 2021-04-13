from bisect import bisect_right

N = int(input())

nums = []
for i in range(1, 10**6):
    nums.append(int(str(i)*2))

nums.sort()
print(bisect_right(nums, N))