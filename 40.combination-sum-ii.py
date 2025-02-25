#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sub = []

        candidates.sort()
        
        def dfs(ind  , target):
            if ind == len(candidates):
                if target == 0 :  
                    result.append(sub[:])
                return
            if candidates[ind] <= target:
                sub.append(candidates[ind])
                dfs(ind + 1 , target - candidates[ind])
                sub.pop()
            
            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind + 1]:
                ind+=1 
            dfs(ind+1 , target)
        
        dfs(0 , target)
        return result
        
# @lc code=end

