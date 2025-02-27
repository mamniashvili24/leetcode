class Solution(object):
    def mySqrt(self, x):
        sqrt = 0
        counter = 0

        while counter <= x:
            sqrt = counter ** 2
            if sqrt > x:
                return counter - 1

            counter += 1                

        return sqrt

sol = Solution()
result = sol.mySqrt(1)
print(result)
print