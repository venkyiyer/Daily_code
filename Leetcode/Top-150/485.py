class Solution:
    def findMaxConsecutiveOnes(self, nums):
        sum_1 = 0
        lst = []
        for i in nums:
            if i == 1:
                sum_1 +=1
            else:
                lst.append(sum_1)
                sum_1 = 0
        
        lst.append(sum_1)
        return max(lst)


obj = Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))