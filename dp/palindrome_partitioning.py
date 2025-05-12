import sys

def isPalindorme(s , i , j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# def solve(s , i , j):
#     if i >= j  or  isPalindorme(s , i , j):
#         return 0
#     res = sys.maxsize
#     for k in range(i , j):
#         temp_res = solve(s , i  , k) + solve(s , k+ 1, j) + 1
#         res = min(res , temp_res)
#     return res
    
# def pp(s):
#     return solve(s , 0 , len(s) -1)


# def solvem(s , i , j , mt):
#     if i >= j or isPalindorme(s , i , j):
#         return 0 
    
#     if mt[i][j] != -1:
#         return mt[i][j] 
    
#     res = sys.maxsize
#     for k in range(i , j):
#         temp_res = solvem(s , i , k , mt) + solvem(s , k +1 , j , mt) + 1
#         res = min(res , temp_res)
#     mt[i][j] = res
#     return res
    
# def ppm(s):
#     mt = [[-1] * len(s) for _ in range(len(s))]
#     return solvem(s , 0 , len(s) -1 , mt)


def solvemm(s  , i , j , mt):
    if i >= j or isPalindorme(s ,  i , j):
        return 0
    
    if mt[i][j] != -1:
        return mt[i][j]
    
    res = sys.maxsize
    for k in range(i , j):
        # temp_res = solvemm(s , i , k , mt) + solvem(s , k +1 , j , mt) + 1
        if mt[i][k] != -1:
            left =   mt[i][k]
        else:
            left = solvemm(s , i , k , mt)
            mt[i][k] = left

        if mt[k+1][j] != -1:
            right = mt[k+1][j]
        else:
            right = solvemm(s , k +1 , j , mt)
            mt[k+1][j] = right
        
        temp_res = left + right + 1

        res = min(res , temp_res)
    mt[i][j] = res
    return res
    

def ppm(s):
    mt = [[-1] * len(s) for _ in range(len(s))]
    return solvemm(s , 0 , len(s) -1 , mt)



if __name__ == "__main__":
    s = 'nitin'
    print(ppm(s))
    s = 'aab'
    print(ppm(s))
    s = 'ababbbabbababa'
    print(ppm(s))
    s = 'civic'
    print(ppm(s))
    s = 'racecar'
    print(ppm(s))
    s = 'aabbcc'
    print(ppm(s))


