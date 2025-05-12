def lcs(s1 , s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1 , n + 1):
        for j in range(1 , m + 1):
            if s1[i-1] == s2[j-1] and i != j :
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i , j = n , m
    lcsString = ''
    while i > 0 and j > 0 : 
        if s1[i-1] == s2[j-1]:
            lcsString = s1[i-1] + lcsString
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            lcsString = s1[i-1] + lcsString
            i -= 1
        else:
            lcsString = s2[j-1] + lcsString
            j -= 1  

     # Add remaining characters
    while i > 0:
        lcsString = s1[i-1] + lcsString
        i -= 1
    while j > 0:
        lcsString = s2[j-1] + lcsString
        j -= 1
    
    return lcsString


if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(lcs(s1, s2))