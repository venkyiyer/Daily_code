class Solution:
    def increasingTriplet(self, nums):
        count = 0
        for i in range(1, len(nums)):
            print(nums[i])
            print(nums[i-1])
            if nums[i] > nums[i-1]:
                count +=1
            
        if count >=3:
            return True
        else:
            return False
            
obj = Solution()
obj.increasingTriplet([2,1,5,0,4,6])