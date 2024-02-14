class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place 
        """
        for i in range(n):
            nums1.pop(-1)

        if len(nums1) == 0:
            for num in nums2:
                nums1.append(num)
            return

        current_nums1_index = 0

        while (current_nums1_index < len(nums1) and len(nums2) > 0):
            num1 = nums1[current_nums1_index]
            num2 = nums2[0]
            if (num2 <= num1):
                nums2.pop(0)
                nums1.insert(current_nums1_index, num2)
                current_nums1_index = 0
                continue

            current_nums1_index += 1

        if (len(nums2) > 0 and len(nums1) > 0):
            if (nums1[0] > nums2[0]):
                for num in nums2:
                    nums1.insert(0,num)
            else:
                for num in nums2:
                    nums1.append(num)

        
