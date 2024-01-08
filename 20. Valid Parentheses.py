class Solution(object):
    def isValid(self, s):

        opens = "({["
        closes = ")}]"
        valids = ["()", "[]", "{}"]

        stack = list()

        for i in s:

            if i in opens:
                stack.append(i)
            
            elif i in closes:
                if len(stack) == 0:
                    return False
                else:
                    j = stack.pop()
                    pair = j + i

                    if pair not in valids:
                        return False


        if len(stack) != 0:
            return False

        return True
