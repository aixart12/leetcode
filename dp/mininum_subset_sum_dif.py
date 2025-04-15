def min_difference(arr):
    n = len(arr)
    arrSum = sum(arr)
    dp = [[False] * (arrSum + 1) for _ in range(n+1)]

    for i in range(n +1):
        dp[i][0] = True
    
    for i in range(1 , n + 1):
        for j in range(1 , arrSum + 1):
            if j < arr[i -1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i -1 ][j - arr[i-1]]
    
    # Find the minimum difference
    min_diff = float('inf')
    
    for sum_val in range(0, arrSum // 2 + 1):
        if dp[n][sum_val]:
            min_diff = min(min_diff, \
                      abs((arrSum - sum_val) - sum_val))
    return min_diff

if __name__ == "__main__":
  
    arr = [1, 6, 11, 5]
    print(min_difference(arr))
