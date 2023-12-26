class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first_num = second_num = 2 ** 31 + 1

        for n in nums:
            if (n < first_num):
                first_num = n
            elif (n < second_num and n != first_num):
                second_num = n
            elif (n > second_num):
                return True

        return False
