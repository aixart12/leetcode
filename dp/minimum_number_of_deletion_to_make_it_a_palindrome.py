# minimum_number_of_deletion_to_make_it_a_palindrome


def lcs(s1 , s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return {
        "deletion" : n - dp[n][m]
    }

if __name__ == "__main__":
    s1 = 'agbcba'
    s2 = s1[::-1]
    print(lcs(s1, s2))