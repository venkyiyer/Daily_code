class solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return i, dic[diff]
            dic[nums[i]] = i

obj = solution()
print(obj.twoSum([3,2,4], 6))