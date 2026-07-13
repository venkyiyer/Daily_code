class Solution:
    def KidswithCandies(self, candies, extraCandies):
        bool_list = []
        max_candies = max(candies)
        for i in candies:
            i+= extraCandies
            if i>= max_candies:
                bool_list.append('true')
            else:
                bool_list.append('false')
        print(bool_list)

obj = Solution()
obj.KidswithCandies([4,2,1,1,2], 1)