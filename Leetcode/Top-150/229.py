from collections import Counter
class Solution:
    def majorityElement(slef, nums):
        majority= []
        max_len = len(nums)/3
        elements = Counter(nums)
        for k, v in elements.items():
            if v > max_len:
                majority.append(k)

        return majority

obj = Solution()
print(obj.majorityElement(nums = [1,2]))
