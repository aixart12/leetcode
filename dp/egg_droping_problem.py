def eggDrop(n, k ):
    # if there is less than or equal to one floor
    if k == 1 or k == 0:
        return k
    
    # if there is only one egg
    if n == 1:
        return k
    
    # to store the minimum number of attempts
    res = float('inf')

     # Consider all droppings from
    # 1st floor to kth floor
    for i in range(1, k + 1):
        cur = 1 + max(eggDrop(n - 1, i - 1), eggDrop(n, k - i))
        if cur < res:
            res = cur
    
    return res

def solveEggDrop(n , k , memo):

    if memo[n][k] != -1:
        return memo[n][k]
    
    if k == 1 or k == 0:
        return k
    
    # if there is only one egg
    if n == 1:
        return k
    
     # to store the minimum number of attempts
    res = float('inf')

    for i in range(1 , k+1):
        curr =  1 + max(solveEggDrop(n-1 , i-1), solveEggDrop(n , k- i))
        if curr < res:
            res = curr

    memo[n][k] =  res + 1

    return memo[n][k]
    


if __name__ == "__main__":
    n = 2
    k = 10
    # create memo table
    memo = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    print(solveEggDrop(n, k, memo))
    print(eggDrop(n, k))