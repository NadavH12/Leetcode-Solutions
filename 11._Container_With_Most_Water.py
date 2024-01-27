class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """2-Pointer Solution O(N)"""

        max_water = 0

        left_index = 0
        right_index = len(height) - 1

        while(right_index > left_index):
            left = height[left_index]
            right = height[right_index]

            shorter_side = min(left,right)

            water = (right_index - left_index) * shorter_side
            if (max_water < water):
                max_water = water

            if (left < right):
                left_index += 1

            elif (right <= left):
                right_index -=1

        return max_water 


        """ Naive Solution O(N^2)
        max_water = 0

        for i in range(len(height)):
            left = height[i]

            for j in range(i, len(height)):
                right = height[j]

                shorter_side = min(left,right)

                water = (j - i) * shorter_side

                if (water > max_water):
                    max_water = water

        return max_water
        """
