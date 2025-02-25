#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        sub = []

        def isPalindrome(s : str , start : int  , end: int) -> bool : 
            while start <=end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True

        def dfs(index):
            if index == len(s):
                result.append(sub[:])
                return
            
            for i in range(index , len(s)):
                if isPalindrome(s , index , i):
                    sub.append(s[index:i + 1])
                    dfs(i+1)
                    sub.pop()
                
            
        dfs(0)  # do partation here
        return result
        
# @lc code=end

