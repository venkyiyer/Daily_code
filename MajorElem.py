class Solution:
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        
        return max(d,key=d.get) 

obj = Solution()
print(obj.majorityElement([3,3,4]))
        