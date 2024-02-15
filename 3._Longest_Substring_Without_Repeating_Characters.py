class Solution(object):

  #brute force solution
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substrings = []

        for i in range(len(s)):
            substring = s[i]
            if substring not in substrings:
                substrings.append(substring)
            for j in range(i+1, len(s)):
                substring += s[j]
                if substring not in substrings:
                    substrings.append(substring)

        maxstring = ""

        for string in substrings:
            if (self.doesntContainDuplicates(string) and len(string) > len(maxstring)):
                maxstring = string


        return len(maxstring)
            

    def doesntContainDuplicates(self, s):
        for char in s:
            if (s.count(char) != 1):
                return False

        return True




#faster brute force
    def lengthOfLongestSubstring(self, s):

        if len(s) == 1:
            return 1


        maxlen = 0

        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1, len(s)):
                occurances = substring.count(s[j])
                if (occurances == 0):
                    substring += s[j]
                if (occurances > 0 or occurances == 0 and j == len(s) - 1):
                    curr_len = len(substring)
                    if (curr_len > maxlen):
                        maxlen = curr_len
                    break

        return maxlen













