class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = max(len(word1),len(word2))
        List = []
        for i in range(n):
            if i < len(word1):
                List.append(word1[i])
            if i < len(word2):
                List.append(word2[i])
        return "".join(List)
                