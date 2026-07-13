class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        count = 0
        for i in range(k):
            count += nums[i]

        max_avg =  count / k 

        for j in range(k,n):
            count+= nums[j]
            count-= nums[j-k]

            avg = count / k

            max_avg = max(max_avg, avg)
        
        return max_avg

obj = Solution()
print(obj.findMaxAverage([1,12,-5,-6,50,3], 4))
