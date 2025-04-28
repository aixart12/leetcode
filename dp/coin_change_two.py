def count(coins, s):
    max_int = float('inf') - 1
    n = len(coins)

    dp = [[0] * (s + 1) for _ in range(n + 1)]

    for i in range(1, s + 1):
        dp[0][i] = max_int

    for j in range(1, s + 1):
        if j % coins[0] == 0:
            dp[1][j] = j // coins[0]
        else:
            dp[1][j] = max_int

    for i in range(2, n + 1):
        for j in range(1, s + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][s] if dp[n][s] != max_int else -1


if __name__ == "__main__":
    coins = [1, 2, 3]
    s = 5
    
    print(count(coins, s))