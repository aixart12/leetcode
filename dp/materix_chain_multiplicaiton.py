import sys
def minMultRec(arr , i , j):
    if i +1 == j :
        return 0
    
    res = sys.maxsize
    
    for k in range(i + 1 , j):
        temp = minMultRec(arr , i , k) + minMultRec(arr , k  , j) +  (arr[i] * arr[k] * arr[j])
        res = min(temp , res)

    return res


def matrixMultiplication(arr):
    n = len(arr)
    return minMultRec(arr, 0, n - 1)

if __name__ == "__main__":
    arr = [2, 1, 3, 4]
    res = matrixMultiplication(arr)
    print(res)

# --------------------------------------------------------------------------------

# def solve(arr,i,j):
#     if i>=j:
#         return 0
#     mn = float('inf')
#     temp=mn
#     for k in range(i,j):
#         temp = solve(arr,i,k) + solve(arr,k+1,j) + (arr[i-1]*arr[k]*arr[j])
#         mn = min(temp,mn)
#     return mn


# def matrixMultiplication(arr):
#     n=len(arr)
#     i=1
#     j=n-1
#     print(solve(arr,i,j))
    

    

# if _name_ == "_main_":
#     arr = [2, 1, 3, 4]
#     matrixMultiplication(arr)