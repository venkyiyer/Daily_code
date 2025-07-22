class Solution:
    def normOfSubarray(self, arr, k, threshold):
        count  = 0
        for i in range(len(arr)-1):
            if len(arr[i:i+k]) == k and sum(arr[i:i+k])//k >= threshold:
                count += 1
        
        return count

obj = Solution()
print(obj.normOfSubarray(arr = [1,1,1,1,1], k = 1, threshold = 0))
