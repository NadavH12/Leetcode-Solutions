class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = 0


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                element = grid[i][j]
                if element == "0" or element == ("1", "X"):
                    continue
                else:
                    islands += 1
                    grid[i][j] = ("1", "X")
                    self.populateIsland(grid, i, j)

        return islands


    def populateIsland(self, grid, i, j):
        if (i > 0):
            if grid[i-1][j] == "1":
                grid[i-1][j] = ("1", "X")
                self.populateIsland(grid, i-1, j)


        if (i < len(grid) - 1):
            if grid[i+1][j] == "1":
                grid[i+1][j] = ("1", "X")
                self.populateIsland(grid, i+1, j)


        if (j > 0):
            if grid[i][j-1] == "1":
                grid[i][j-1] = ("1", "X")
                self.populateIsland(grid, i, j-1)

        if (j < len(grid[i]) - 1):
            if grid[i][j+1] == "1":
                grid[i][j+1] = ("1", "X")
                self.populateIsland(grid, i, j+1)
