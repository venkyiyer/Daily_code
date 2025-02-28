words = ["cat","bt","hat","tree"]
chars = "atach"

from collections import Counter
from collections import defaultdict
class Solution:
    def countCharacters(self, words, chars):
        count_chars = Counter(chars)
        count = 0
        for w in words:
            current_word = defaultdict(int)
            good = True
            for i in w:
                current_word[i]+=1
                if i not in count_chars or current_word[i] > count_chars[i]:
                    good = False
                    break
            if good:
                count += len(w)
        
        return count
    
obj = Solution()
print(obj.countCharacters(words, chars))