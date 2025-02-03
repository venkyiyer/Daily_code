nums = [1,3,4,2]

class Solution:
    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
                if d[i] >=2:
                    return True
        return False

obj = Solution()
print(obj.containsDuplicate(nums))

