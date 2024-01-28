class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret_list = []

        #add first row 
        #add last column
        #add last row
        #add first column 
        #repeat 

        #handle column matrix
        if (len(matrix[0]) == 1):
            for row in matrix:
                ret_list += row
            return ret_list

        #spiral
        while (len(matrix) > 1 and len(matrix[0]) > 1):
            next_list = self.get_matrix_elements(matrix)
            ret_list += next_list
            matrix = self.reduce_matrix(matrix)

        if (matrix == []):
            return ret_list

        #handle leftover column matrix
        if (len(matrix[0]) == 1):
            for row in matrix:
                ret_list += row
            return ret_list


        #handle leftover row matrix 
        if (len(matrix) > 0):
            ret_list += matrix[0]

        return ret_list



    def get_matrix_elements(self, matrix):
        next_list = []
        height = len(matrix)
        length = len(matrix[0])

        first_row = matrix[0]
        for i in first_row:
            next_list.append(i)

        for i in range(1, height - 1):
            row = matrix[i]
            next_list.append(row[length-1])

        last_row = matrix[height - 1]
        for i in range(length-1,-1,-1):
            next_list.append(last_row[i])

        for i in range(height-2,0,-1):
            row = matrix[i]
            next_list.append(row[0])

        return next_list

    

    def reduce_matrix(self, matrix):
        height = len(matrix)
        for i in range(0, height - 1):
            row = matrix[i]
            row.pop(0)
            if (len(row) > 0):
                row.pop()

        matrix.pop(0)
        matrix.pop()

        return matrix
