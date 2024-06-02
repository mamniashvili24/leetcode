class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1
        result = base
        for i in range(abs(exponent) - 1):
            result *= base
        if exponent < 0:
            result = 1 / result
        return result

print(Solution().myPow(2.00000, 0))