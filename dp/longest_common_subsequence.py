# [Naive Approach] Using Recursion – O(2 ^ min(m, n)) Time and O(min(m, n)) Space

# def lcsRec(s1 , s2 , m ,n):
#     if m == 0 or n == 0:
#         return 0
    
#     if s1[m-1] == s2[n-1]:
#         return 1 + lcsRec(s1 , s2 , m-1 , n-1)
#     else:
#         return max(lcsRec(s1 , s2 , m-1 , n) , lcsRec(s1 , s2 , m , n-1))
    
# def lcs(s1,s2):
#     m = len(s1)
#     n = len(s2)
#     return lcsRec(s1,s2,m,n)

# if __name__ == "__main__":
#     s1 = "AGGTAB"
#     s2 = "GXTXAYB"
#     print(lcs(s1, s2))

# [Better Approach] Using Memoization (Top Down DP) – O(m * n) Time and O(m * n) Space

# def lcsRec(s1,s2,m,n, memo):
#     if m == 0 or n == 0 :
#         return 0 
#     if memo[m][n] != -1 :
#         return memo[m][n]
    
#     if s1[m-1] == s2[n-1]:
#         memo[m][n] = 1 + lcsRec(s1 , s2 , m , n , memo)
#         return memo[m][n]
#     else:
#         memo[m][n] = max(lcsRec(s1 , s2 , m-1 , n , memo) , lcsRec(s1 , s2 , m , n-1 , memo))
#     return memo[m][n]

# def lcs(s1,s2):
#     m = len(s1)
#     n = len(s2)
#     memo = [[-1  for _ in range(m + 1)] for _ in range(n + 1)]
#     return lcsRec(s1,s2,m,n, memo)

# if __name__ == "__main__":
#     s1 = "AGGTAB"
#     s2 = "GXTXAYB"
#     print(lcs(s1, s2))

# [Expected Approach 1] Using Bottom-Up DP (Tabulation) – O(m * n) Time and O(m * n) Space


def lcsDp(s1 , s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1 , n + 1):
        for j in range(1 , m + 1):
            if s1[j -1] == s2[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[n][m]

if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"

    print(lcsDp(s1, s2))
