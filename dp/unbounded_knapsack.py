def knapSack(capacity , val , wt):
    n = len(val)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):  # start from 0
            pick = 0
            notPick = dp[i - 1][j]

            if wt[i - 1] <= j:
                pick = val[i - 1] + dp[i][j - wt[i - 1]]  # use dp[i], not dp[i-1]
        
            dp[i][j] = max(notPick, pick)

    return dp[n][capacity]


if __name__ == "__main__":
    val = [1, 1]
    wt = [2, 1]
    capacity = 3
    print(knapSack(capacity, val, wt))  # Output: 3
