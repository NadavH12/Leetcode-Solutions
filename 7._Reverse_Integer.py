class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)
        negative = False

        if (x < 0):
            negative = True
            s = s[1:]


        s_rev = ""
        for i in range(len(s)-1, -1, -1):
            s_rev += s[i]
        
        ret_val = int(s_rev)

        if (negative):
            ret_val *= -1


        if (ret_val < -2**31 or ret_val > 2**31 -1):
            ret_val = 0
     

        return ret_val
        
