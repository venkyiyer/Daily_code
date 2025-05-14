from collections import Counter
class Solution:
    def divideArray(self, nums):
        count = Counter(nums)
        for i in count:
            print(count[i])
            if count[i]%2 == 0:
                continue
            else:
                return False
        
        return True

obj = Solution()
print(obj.divideArray([1,2,1,2,500,52]))
