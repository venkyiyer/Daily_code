class Solution:
    def longestSubarray(self,nums):
        count_0 = 1
        l = 0
        for i in range(len(nums)):
            count_0 -= nums[i] == 0

            if count_0<0:
                count_0 += nums[l] == 0
                l +=1
        
        return i - l 
