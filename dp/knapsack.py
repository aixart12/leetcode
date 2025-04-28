# 1 . subset sum 
# 2 . Equal Sum partation 
# 3 . Count of subset sum 
# 4 . Minium subset sum diff
# 5 . Target sum 
# # of teh subset & given d/f

# Type of knapsack 
    # Fractional knpasack ( can brake the item into fraction ) --> Greedy 
    # 0 / 1 ( ya to hoga , ya to nahi , or ek he har )
    # unbound knapseek ( 0/ 1 but ek ko bar bar dal sakte hai , multiple occurance )


# subset sum problem 
# Using Recursion O(2^n) Time and O(n) Space

def knapsackRec(W , val , wt , n):

    # Base case
    if n == 0 or W == 0:
        return 0
    
    pick  = 0 

    # Pick nth item if it doesn't exceed the capacity of knapsack 

    if wt[n-1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1] , val , wt , n - 1)
    
    # Don't pick the nth item 

    notPick = knapsackRec(W , val , wt , n-1)

    return max(pick , notPick)

def knapSack(W , val , wt):
    n = len(val)
    return knapsackRec(W , val , wt , n)

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapSack(W, val, wt))

# Using Bottom-Up DP (Tabulation) – O(n x W) Time and Space
def knapsack(W, val, wt):
    n = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the dp table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(W + 1):
            # If the item can be picked
            if wt[i - 1] <= j:
                pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                notPick = dp[i - 1][j]
                dp[i][j] = max(pick, notPick)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]

# Example usage
if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))  # Output should be 3


# Using Bottom-Up DP (Space-Optimized) – O(n x W) Time and O(W) Space

# Function to find the maximum profit
def knapsack(W, val, wt):
    
    # Initializing dp list
    dp = [0] * (W + 1)

    # Taking first i elements
    for i in range(1, len(wt) + 1):
        
        # Starting from back, so that we also have data of
        # previous computation of i-1 items
        for j in range(W, wt[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])
    
    return dp[W]

if __name__ == "__main__":
    val = [1, 2, 3]
    wt = [4, 5, 1]
    W = 4

    print(knapsack(W, val, wt))
