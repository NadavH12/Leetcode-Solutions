class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open_indices = list()
        star_indices = list()

        for i in range(len(s)):
            char = s[i]

            if char == "(":
                open_indices.append(i)

            elif char == "*":
                star_indices.append(i)

            elif char == ")":
                if len(open_indices) > 0:
                    open_indices.pop()
                elif len(star_indices) > 0:
                    star_indices.pop()
                else:
                    return False


        
        while len(open_indices) != 0 and len(star_indices) != 0:
            last_open = open_indices.pop()
            last_star = star_indices.pop()

            if last_open > last_star:
                return False


        return len(open_indices) == 0
