from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasset = set()
        for num in nums:
            if num in hasset:
                return True
            hasset.add(num)
        return False