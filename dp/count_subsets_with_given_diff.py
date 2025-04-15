# Example usage
def count_subsets_with_given_diff(arr , diff):
    target = (diff + sum(arr)) // 2

    n = len(arr)

    dp = [ [0] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1 
    
    for i in range(1 , n+1):
        for  j in range(1 , target + 1):
            if j < arr[i -1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j - arr[i - 1]]
            
    return dp[n][target]


if __name__ == "__main__":
    arr = [1, 1, 2, 3]
    diff = 1
    print("Count of subsets with given difference is:", count_subsets_with_given_diff(arr,diff))