class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        index = 0

        while (index < len(word1) and index < len(word2)):
            result += word1[index]
            result += word2[index]
            index += 1

        while (index < len(word1)):
            result += word1[index]
            index += 1

        while (index < len(word2)):
            result += word2[index]
            index += 1
        

        return result
        
