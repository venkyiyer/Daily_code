nums = [1,1]

class Solution:
    def findDisappearedNumbers(self, nums):
        nums1 = []
        nums2 = [i for i in range(1, len(nums)+1)]
        for i in range(len(nums2)):
            if nums2[i] not in nums:
                nums1.append(nums2[i])

        return nums1

obj=Solution()
print(obj.findDisappearedNumbers(nums))


# for n in nums:
#             i = abs(n) - 1
#             nums[i] = -1 * abs(nums[i])
        
#         res = []
#         for i, n in enumerate(nums):
#             if n > 0:
#                 res.append(i+1)

#         return res