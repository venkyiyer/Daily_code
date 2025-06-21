class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l<r:
            currSum = numbers[l] + numbers[r]

            if currSum> target:
                r-=1
            elif currSum < target:
                l +=1
            else:
                return [l+1, r+1]

        return []
            


obj = Solution()
print(obj.twoSum([2,7,11,15], 9))

    