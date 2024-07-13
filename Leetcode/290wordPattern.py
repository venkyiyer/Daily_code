class Solution:
    def wordPattern(self, pattern, s):
        s = s.split(' ')
        st_map = {}
        for c1, c2 in zip(pattern,s):
            if c1 not in st_map:
                st_map[c1] = c2
            else:
                if st_map[c1]!= c2:
                    return False
        
        return True


obj = Solution()
print(obj.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))