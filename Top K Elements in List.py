from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, numbers: List[int], top_n: int) -> List[int]:
        number_counts = {number: numbers.count(number) for number in numbers}
        result = dict(sorted(number_counts.items(), key=lambda x: x[1]))
        return list(result)[-top_n:]

print(Solution().topKFrequent([1,1,1,2,2,3], 2))