nums = [1,3,5,6]
target = 5

class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        
        while l<= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid  -1
            
            else:
                l = mid +1
        
        return l 

obj = Solution()
print(obj.searchInsert(nums, target))