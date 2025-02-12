nums = [3,3,4]
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        n=len(nums)
        return nums[n//2]
        
obj = Solution()    
print(obj.majorityElement(nums))




# d = {}
#         for i in range(len(nums)):
#             if nums[i] not in d:
#                 d[nums[i]] =1
#             else:
#                 d[nums[i]]+=1
        
#         k = max(d, key= d.get)
#         print(k)
#         print(d[k])
#         if d[k] > len(nums)/2:
#             return True


# result, count = 0, 0

#         for i in nums:
#             if count == 0:
#                 result = i
#             count += (1 if i == result else -1)
#         return result