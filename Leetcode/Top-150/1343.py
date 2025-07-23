class Solution:
    def normOfSubarray(self, arr, k, threshold):
        count  = 0
        for i in range(len(arr)):
            print('arr->', arr[i:i+k])
            if len(arr[i:i+k]) == k and sum(arr[i:i+k])//k >= threshold:
                count += 1
        
        return count

obj = Solution()
print(obj.normOfSubarray(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
