class Solution:
    def compress(self, chars):
        get_numbers = {}
        for i in chars:
            if i not in get_numbers:
                get_numbers[i]=1
            else:
                get_numbers[i] +=1

        print(get_numbers)


obj = Solution()
obj.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
