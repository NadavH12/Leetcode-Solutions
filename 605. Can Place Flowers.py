class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        if (len(flowerbed) == 1):
            if (flowerbed[0] == 0):
                return (n <= 1)
            else:
                return (n <= 0)

        valid_plots = 0
        if (flowerbed[1] + flowerbed[0] == 0):
            valid_plots += 1
            flowerbed[0] = 1


        for index in range(1, len(flowerbed) - 1):
            current_plot = flowerbed[index]
            if (current_plot == 0):
                left_plot = flowerbed[index - 1]
                right_plot = flowerbed[index + 1]
                if (left_plot + right_plot == 0):
                    valid_plots += 1
                    flowerbed[index] = 1


        if (flowerbed[len(flowerbed) - 1] + flowerbed[len(flowerbed) - 2] == 0):
            valid_plots += 1
            flowerbed[len(flowerbed) - 1] = 1

        return (valid_plots >= n)