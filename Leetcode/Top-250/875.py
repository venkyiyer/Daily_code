class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        while low < high:
            hours = 0
            mid = (low + high) // 2
            for i in piles:
                hours += i // mid
                if i % mid !=0:
                    hours +=1

            if hours <= h:
                high = mid
            else:
                low = mid + 1

        return low

obj = Solution()
print(obj.minEatingSpeed(piles = [1,4,3,2], h = 9))

