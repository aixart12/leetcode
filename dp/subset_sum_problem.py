def isSubsetSumRec(arr, n, sum):

    if sum == 0 :
        return True
    if n == 0 : 
        return False
    
    if arr[n-1] > sum:
        isSubsetSumRec(arr , n-1 , sum)
    
    return isSubsetSumRec(arr, n - 1, sum) or isSubsetSumRec(arr, n - 1, sum - arr[n - 1])


def isSubsetSum(arr, sum):
    return isSubsetSumRec(arr , len(arr) , sum)

if __name__ == "__main__":
  
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9

    if isSubsetSum(arr, sum):
        print("True")
    else:
        print("False")

#  Using Top-Down DP (Memoization) – O(sum*n) Time and O(sum*n) Space

def isSubsetSumRec(arr, n , sum , memo):

    if sum == 0 : 
        return True
    if n == 0 : 
        return False
    
    if memo[n][sum] !=  -1 : 
        return memo[n][sum]
    
    if arr[n -1] > sum:
        memo[n][sum] = isSubsetSumRec(arr , n-1 , sum , memo)
    else:
        memo[n][sum] = (isSubsetSumRec(arr , n-1 , sum) or isSubsetSumRec(arr , n-1 , sum - arr[n-1]))

    return memo[n][sum]

def isSubsetSum(arr, sum):
    n = len(arr)
    memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
    return isSubsetSumRec(arr, n, sum, memo)


if __name__ == "__main__":
    arr = [1, 5, 3, 7, 4]
    sum = 12

    if isSubsetSum(arr, sum):
        print("True")
    else:
        print("False")

# [Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) Time and O(sum*n) Space

def isSubsetSum(arr, sum):
    n = len(arr)

    dp = [[False] * (sum + 1) for _ in range(n +1 )]

    for i in range(n +1) : 
        dp[i][0] = True
    
    for i in range(1 , n+1):
        for j in range(1 , sum +1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or  dp[i-1][j-arr[i - 1]]
    
    return dp[n][sum]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9

    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")

# [Expected Approach] Using Space Optimized DP – O(sum*n) Time and O(sum) Space

def isSubsetSum(arr, sum):
    n = len(arr)

    pev = [False] * (sum+1)
    curr = [False] * (sum + 1)

    pev[0] = True

    # Fill the dp table in a
    # bottom-up manner
    for i in range(1  , n + 1):
        for j in range( 1 , sum + 1):
            if j < arr[n - 1]:
                curr[j] = pev[j]
            else:
                curr[j] = pev[j] or pev[j - arr[i - 1]]
        pev = curr.copy()

    return pev[sum]



if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9
    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")