from bisect import bisect_left

X = int(input())

valids = set(range(10))

nums = set()
for i in range(1, 19):
    for first in range(1, 10):
        for diff in range(-9, 10):
            l = [None]*i
            l[0] = first
            for j in range(i-1):
                l[j+1] = l[j] + diff
            if set(l) - valids == set():
                num = int(''.join(map(str, l)))
                nums.add(num)

all_nums = sorted(nums)
# print(all_nums)
ans_idx = bisect_left(all_nums, X)
ans = all_nums[ans_idx]
print(ans)
