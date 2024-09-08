from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            for num1 in nums:
                if  num == num1:
                    return True
        return False


print(Solution().hasDuplicate([1,2,3,4]))
