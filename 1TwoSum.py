class solution:

    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

obj = solution()
print(obj.twoSum([2,7,11,15], 9))