"""
Problem: Find all combinations that sum meets the target.

Solution:
1. We use the backtracking approach and for inside to optimize the solution by ridding of the duplicates.

Time: O(2*t/m)
Space: O(t/m), where t is target, m  is the minimum value in nums.
"""

from typing import List


def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    comb, currComb = [],[]

    def helper(i, currSum):
        if currSum == target:
            comb.append(currComb.copy())
            return
        elif currSum > target:
            return
        elif i > len(nums):
            return


        for j in range(i, len(nums)):
            val = nums[j]
            currComb.append(val)
            currSum += val
            helper(j, currSum)
            currComb.pop()
            currSum -= val

    helper(0, 0)

    return comb


combination = combinationSum([1,2,9], 2)
print(combination)
