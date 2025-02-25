#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sub = []

        def dfd( ind , target):
            if ind == len(candidates):
                if target == 0 :
                   result.append(sub[:])
                return
            if candidates[ind] <= target : 
               sub.append(candidates[ind])
               if target == 0:
                   result.append(sub[:])
                   return
               dfd(ind , target-candidates[ind])
               sub.pop()
            dfd(ind + 1 , target)

        dfd(0 , target)
        return result
       
# @lc code=end

