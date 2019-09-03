def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

class Heap:
    def __init__(self, nums):
        self.nums_len = 0
        self.nums = []
        for num in nums:
            self.insert(num)

    
    def insert(self, num):
        self.nums.append(num)
        # print(self.nums)
        self.nums_len += 1

        index = self.nums_len-1
        while not (index == 0 or self.nums[index] > self.nums[(index-1)//2]):
            # print(f"index: {index}, par: {(index-1)//2}")
            # print(self.nums[index], self.nums[(index-1)//2])
            swap(self.nums, index, (index-1)//2)
            # self.nums[index], self.nums[(index-1)//2] = self.nums[(index-1)//2], self.nums[index]
            index = (index-1)//2
            # print(self.nums, self.nums_len)
        # x = 0
        # while 2**x <= self.nums_len:
        #     print(*self.nums[2**x-1:2**(x+1)-1], sep=" ")
        #     x += 1
        # print()

# l = list(range(32))[::-1]
# h = Heap(l)
# print(h.nums)
# x = 0
# while 2**x < len(h.nums):
#     print(*h.nums[2**x:2**(x+1)], sep=" ")
#     x += 1
