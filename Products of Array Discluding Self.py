from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            elements_except_i = nums[:i] + nums[i+1:]
            multiprocessing = 1
            for j in elements_except_i:
                multiprocessing *= j
            result.append(multiprocessing)
        return result