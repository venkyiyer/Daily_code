class Solution:
    def isCircularSentence(self, sentence):
        sent = sentence.split(" ")
        if len(sent)==1:
            if sent[0][0] == sent[0][-1]:
                return True
        for i in range(len(sent)-1):
            if sent[i][-1] == sent[i+1][0]:
                continue
            else:
                return False
        
        return sent[-1][-1] == sent[0][0]

obj = Solution()
print(obj.isCircularSentence("Leetcode eisc cool"))

