class Solution:
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == k:
                    count +=1
                    break
        
        return count

obj = Solution()
print(obj.subarraySum(nums=[1,2,3], k =3))