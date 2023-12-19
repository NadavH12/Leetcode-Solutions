class Solution(object):

    def gcd(self, a, b):
        if(b == 0):
            return a
        else:
            return self.gcd(b, a % b)

    def gcdOfStrings(self, str1, str2):
        if (str1 + str2 != str2 + str1):
            return ""
        elif (str1 == str2):
            return str1

        gcd_length = self.gcd(len(str1), len(str2))
        gcd = str1[0:gcd_length]
        return gcd