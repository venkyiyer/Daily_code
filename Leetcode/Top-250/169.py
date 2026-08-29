class Solution:
    def majorityElement(self, nums):
        l = len(nums)/2
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i]=1
        
        if max(d.values()) > l:
            return max(d, key=d.get)
