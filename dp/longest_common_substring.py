def lcsDp(s1 , s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_length = 0

    for i in range(1 , n + 1):
        for j in range(1 , m + 1):
            if s1[j -1] == s2[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
            else:
                dp[i][j] = 0 
    return max_length

if __name__ == "__main__":
    s1 = "GAGGTAB"
    s2 = "GAXTXAYB"

    print(lcsDp(s1, s2))