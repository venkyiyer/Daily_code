nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

class Solution:
    def intersection(self, nums1, nums2):
        intersection_elements = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] not in intersection_elements:
                    intersection_elements.append(nums1[i])
        
        return intersection_elements

obj = Solution()
print(obj.intersection(nums1, nums2))


