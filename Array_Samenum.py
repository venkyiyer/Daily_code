class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor

obj = Solution()
print(obj.singleNumber([4,1,2,1,2]))
        
