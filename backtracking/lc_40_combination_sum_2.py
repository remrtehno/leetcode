"""
Problem:

Solution:
1. Backtracking with sorting and optimization

Time: O(2n)
Space: O(k), where k is elements of....
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sub, res = [], []

        def dfs(i, curSum):
            if curSum == target:
                res.append(sub.copy())
                return
            if i > len(candidates):
                return

            for j in range(i, len(candidates)):
                sub.append(candidates[i])
                dfs(j + 1)
                sub.pop()

        dfs(0, 0)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb, curCombs = [], []
        candidates.sort()

        def helper(i, curSum):
            if curSum == target:
                comb.append(curCombs.copy())
                return
            if curSum > target:
                return
            if i > len(candidates) - 1:
                return

            j = i
            while j < len(candidates):
                curVal = candidates[j]
                curCombs.append(curVal)
                helper(j + 1, curVal + curSum)
                curCombs.pop()
                while j + 1 < len(candidates) and candidates[j] == candidates[j + 1]:
                    j += 1
                j += 1

        helper(0, 0)
        return comb



