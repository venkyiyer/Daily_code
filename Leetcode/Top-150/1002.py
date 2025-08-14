from collections import Counter
class Solution:
    def commonChar(self, words):
        cnt = Counter(words[0])

        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])
        
        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        
        return res

