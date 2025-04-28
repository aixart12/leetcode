def rodCutting(prices, rod_length):
    n = len(prices)
    dp = [[0] * (rod_length + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        length = i  # rod length = i
        for j in range(1, rod_length + 1):
            notCut = dp[i - 1][j]
            cut = 0
            if length <= j:
                cut = prices[i - 1] + dp[i][j - length]

            dp[i][j] = max(notCut, cut)

    return dp[n][rod_length]


if __name__ == "__main__":
    prices = [2, 5, 7, 8]  # price for lengths 1, 2, 3, 4
    rod_length = 5
    print(rodCutting(prices, rod_length))  # Output: 12 (2+2+2+2+2 or 5+5+2 etc.)
