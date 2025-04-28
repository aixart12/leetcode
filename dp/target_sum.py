# You are given an array of non-negative integers arr and an integer target.

# Your task is to assign a '+' or '-' sign to each element in arr such that the final sum of all elements (after applying the signs) is equal to target.

# Return the total number of different ways you can assign these signs to reach the target sum.

# Example usage


def count_target_sum_ways(arr , target):
    n = len(arr)
    newTarget = (target + sum(arr)) // 2

    dp = [[0] * (newTarget + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1 , n+1):
        for j in range(1 , newTarget + 1):
            if j < arr[i -1]:
                dp[i][j] = dp[i  - 1][j]
            else:
                dp[i][j] = dp[i -1][j] + dp[i -1][j -arr[i -1]]

    return dp[n][newTarget]



if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1]
    target = 3
    print("Number of ways to assign +/- to reach target:", count_target_sum_ways(arr,target))