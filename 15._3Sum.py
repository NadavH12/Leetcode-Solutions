class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #Naive Solution O(N^3)
        ret_list = list(list())
        sorted_ret_list = list()

        for i in range(0, len(nums)):
            x = nums[i]
            for j in range(i + 1, len(nums)):
                y = nums[j]
                inner_list = list()
                for k in range(j + 1, len(nums)):
                    z = nums[k]

                    if (x + y + z == 0):
                        inner_list.append(x)
                        inner_list.append(y)
                        inner_list.append(z)

                        sorted_inner_list = set(inner_list)

                        if (sorted_inner_list not in sorted_ret_list):
                            ret_list.append(inner_list)
                            sorted_ret_list.append(sorted_inner_list)
                            break
                            
        return ret_list
        
