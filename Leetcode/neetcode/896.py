nums = [1,1,2]

class Solution:
    def isMonotonic(self, nums):
        getmax = max(nums[:2])
        getmaxindex = nums.index(getmax)
        if getmaxindex == 1:  
            for i in range(len(nums)-1):
                print(nums[i])
                print(nums[i+1])
                if nums[i]<= nums[i+1]:
                    continue
                else:
                    return False
        else:     
            for j in range(len(nums)-1, 0, -1):
                print(nums[j])
                print(nums[j-1])
                if nums[j]<= nums[j-1]:
                    continue
                else:
                    return False
        return True

obj = Solution()
print(obj.isMonotonic(nums))