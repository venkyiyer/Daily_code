class Solution:
    def mostWordsFound(self, sentences: List[str]):
        max_length = []
        for i in sentences:
            splitting = i.split(' ')
            max_length.append(len(splitting))

        return max(max_length)