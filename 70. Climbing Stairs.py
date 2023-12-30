"""
Naive Solution

    def climbStairs(self, n):
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


"""
"""
    Naive Solution W/ Caching

    def climbStairs(self, n):
        cache = dict()
        return self.helper(n, cache)

    def helper(self, n, cache):
        if (n == 0):
            return 0

        if (n == 1):
            return 1

        if (n == 2):
            return 2

        
        cached_val = cache.get(n)

        if (cached_val != None):
            return cached_val


        else:
            cached_val = self.climbStairs(n - 1) + self.climbStairs(n-2)
            cache[n] = cached_val
            return cached_val
"""

"""
Bottom-up solution, using linear space
class Solution:
    def climbStairs(self, n):
        if (n == 0):
            return 0

        if (n == 1):
            return 1

        if (n == 2):
            return 2

        cache = [0] * (n+1)

        cache[0] = 1
        cache[1] = 1

        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
"""

#Bottom-up solution, using constant space 
class Solution:
    def climbStairs(self, n):
        if (n == 0):
            return 0

        if (n == 1):
            return 1

        if (n == 2):
            return 2

        a = 1
        b = 2

        for i in range(3, n+1):
            c = a + b
            a = b
            b = c

        return c
