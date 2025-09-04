class Solution:
    def mergeArrays(self, nums1, nums2):
        i, j = 0,0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i+=1
            elif nums1[i][0] > nums2[j][0]:
                result.append(nums2[j])
                j +=1
            else:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])            
                i+=1
                j+=1
        
        while i < len(nums1):
            result.append(nums1[i])
        
        while j < len(nums2):
            result.append(nums2[j])
        
        return result

obj = Solution()
print(obj.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))

