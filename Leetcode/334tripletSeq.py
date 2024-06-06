class Solution:
    def increasingTriplet(self, nums):
        n1 = n2 = float('inf')
        for i in (nums):
            if i < n1:
                n1 = i
            elif i < n2:
                n2 = i
            else:
                return True    
        return False
            
obj = Solution()
print(obj.increasingTriplet([1,2,1,3]))