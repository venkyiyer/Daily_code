nums = [1,2,3,1] 
k = 3

class Solution:
    def containsNearbyDuplicate(self, nums,k):
        window = set()
        l = 0
        for r in range(len(nums)):
            if r-l> k:
                window.remove(nums[l])
                l +=1
            if nums[r] in window:
                return True
        return False

obj = Solution()
print(obj.containsNearbyDuplicate(nums, k))