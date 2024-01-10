class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        terms_list = list()

        sublist = list()
        for i in range(n, 0, -1):
            if len(sublist) == 4:
                terms_list.append(sublist)
                sublist = list()
                sublist.append(i)

            elif i == 1:
                sublist.append(i)
                terms_list.append(sublist)
                sublist = list()

            else:
                sublist.append(i)
        #print(terms_list)
                
        if len(sublist) > 0:
            terms_list.append(sublist)

        sums = list()

        for sublist in terms_list:
            Sum = sublist[0]
            if len(sublist) == 4:
                Sum *= sublist[1]
                Sum //= sublist[2]
                sums.append(Sum)
                sums.append(sublist[3])

            elif len(sublist) == 3:
                Sum *= sublist[1]
                Sum //= sublist[2]
                sums.append(Sum)

            elif len(sublist) == 2:
                Sum *= sublist[1]
                sums.append(Sum)

            else:
                sums.append(Sum)
        #print(sums)

        final_sum = sums[0]

        for i in range(1, len(sums)):
            if i % 2 == 1:
                final_sum += sums[i]
            else:
                final_sum -= sums[i]

        return final_sum
