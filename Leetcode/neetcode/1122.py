class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    arr.append(j)
        
        return arr

obj = Solution()
print(obj.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))