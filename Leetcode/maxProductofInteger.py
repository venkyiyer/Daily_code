class Solution:
    def maxProduct(self,arr):
        arr.sort()
        return arr[-1] * arr[-2]
            
