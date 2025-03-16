nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

# class Solution:
#     def findDifference(self, nums1, nums2):
#         answer = [[],[]]
#         for i in nums1:
#             if i not in nums2:
#                 if i not in answer[0]:
#                     answer[0].append(i)
        
#         for j in nums2:
#             if j not in nums1:
#                 if j not in answer[1]:
#                     answer[1].append(j)
        
#         return answer

# obj = Solution()
# print(obj.findDifference(nums1, nums2))

class Solution:
    def findDifference(self, nums1, nums2):
        n1 = set(nums1)
        n2 = set(nums2)

        return [list(n1.difference(n2)), list(n2.difference(n1))]

obj = Solution()
print(obj.findDifference(nums1, nums2))

