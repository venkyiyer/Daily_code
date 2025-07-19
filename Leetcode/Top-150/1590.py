class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0
        
        res = len(nums)
        cur_sum = 0
        remainder_index = {0:-1}

        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remainder + p) % p
            if prefix in remainder_index:
                length = i - remainder_index[prefix]
                res = min(res, length)
            remainder_index[cur_sum] = i
        
        return -1 if res == len(nums) else res
    
