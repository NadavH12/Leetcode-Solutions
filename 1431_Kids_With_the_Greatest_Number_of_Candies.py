class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = 0
        result = list()
        

        for candy_count in candies:
            if (candy_count > maximum):
                maximum = candy_count

        

        for candy_count in candies:
            if (candy_count + extraCandies >= maximum):
                result.append(True)
            else:
                result.append(False)

        return result
