class Solution:
    def compress(self, chars):
        l = len(chars)
        i, j = 0,0
        while i < l:
            count = 1
            while i < l and chars[i] == chars[i+1]:
                count +=1
                i +=1
            chars[j] = chars[i]
            j +=1
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j +=1
            i += 1

        return j


obj = Solution()
print(obj.compress(["a","a","b","b","c","c","c"]))
