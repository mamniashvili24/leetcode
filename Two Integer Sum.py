from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previus_map = {}
        for i, value in enumerate(nums):
            difference = target - value
            if difference in previus_map:
                return [previus_map[difference], i]
            previus_map[value] = i
        return []