nums = [9,4,1,7]
k = 2

class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        l, r= 0, k -1
        res = float('inf')

        while r < len(nums):
            print(nums[r])
            print(nums[l])
            res = min(res, nums[r] - nums[l])
            l, r = l +1, r+1
        
        return res

obj = Solution()
print(obj.minimumDifference(nums, k))


