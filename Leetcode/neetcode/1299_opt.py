arr = [17,18,5,4,6,1]

class Solution():
    def replaceElements(self, arr):
        initialMax = -1
        for i in range(len(arr)-1, -1,-1):
            newMax = max(initialMax, arr[i])
            arr[i] = initialMax
            initialMax = newMax
        
        return arr

obj = Solution()
obj.replaceElements(arr)