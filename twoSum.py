from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousDiffs = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in previousDiffs:
                return [previousDiffs[diff], i]
            previousDiffs[n] = i


sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)
