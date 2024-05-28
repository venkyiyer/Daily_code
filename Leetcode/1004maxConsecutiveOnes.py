class Solution:
    def longestOnes(self, nums, k):
        max_w = 0
        l = 0
        no_of_zeros = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                no_of_zeros+=1
        
            while no_of_zeros>k:
                if nums[l] == 0:
                    no_of_zeros -=1
                l+=1

            
            w = r - l +1 
            max_w  = max(max_w, w)

        return max_w

obj = Solution()
obj.longestOnes([1,1,1,0,0,0,1,1,1,1], k = 2)