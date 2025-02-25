#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result= []
        nums.sort()
        def subsets(index , elements):
            # base case
            if index == len(nums):
                result.append(elements) if elements not in result else None
                return
            subsets(index + 1 , elements) # not pick
            subsets(index+1 , elements + [nums[index]]) # pick  
        
        subsets(0 , [])
        return result
    
        
# @lc code=end

