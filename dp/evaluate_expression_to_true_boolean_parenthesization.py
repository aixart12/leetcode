

def evaluate(b1, b2, op):
    if op == '&':
        return b1 & b2
    elif op == '|':
        return b1 | b2
    return b1 ^ b2

def countRecur(i, j, req, s):
    if i == j :
        return 1 if req == (s[i] == 'T') else 0
    
    ans = 0 
    for  k in range(i + 1 , j , 2):
        leftTrue = countRecur(i , k- 1 , True , s)
        leftFalse  = countRecur(i , k-1 , False , s)
        rightTrue = countRecur(k + 1 , j , True , s)
        rightFalse = countRecur(k + 1 , j , False , s)

        if evaluate( True , True , s[k]) == req : 
            ans += leftTrue * rightTrue
        if evaluate(True, False, s[k]) == req:
            ans += leftTrue * rightFalse
        if evaluate(False, True, s[k]) == req:
            ans += leftFalse * rightTrue
        if evaluate(False, False, s[k]) == req:
            ans += leftFalse * rightFalse

    return ans



def countWays(s):
    n = len(s)
    return countRecur(0, n - 1, True, s)

def countRecurM(i , j , req , s , memo):
    if i == j : 
        return 1 if req == (s[i] == 'T') else 0 
    
    if memo[i][j][req] != -1:
        return memo[i][j][req]
    
    ans = 0 
    for k in range( i+ 1 , j , 2):
        leftTrue = countRecurM(i , k - 1 , 1 , s , memo)
        leftFalse = countRecurM(i , k - 1 , 0 , s , memo)
        rightTrue = countRecurM(k + 1 , j , 1  , s , memo)
        rightFalse = countRecurM(k + 1 , j , 0  , s , memo)

        if evaluate( 1 , 1 , s[k]) == req : 
            ans += leftTrue * rightTrue
        if evaluate(1, 0, s[k]) == req:
            ans += leftTrue * rightFalse
        if evaluate(0, 1, s[k]) == req:
            ans += leftFalse * rightTrue
        if evaluate(0, 0, s[k]) == req:
            ans += leftFalse * rightFalse

    memo[i][j][req] = ans
    return ans


def coutWaysM(s):
    n = len(s)
    memo = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n) ]
    return countRecurM(0  ,n -1 , 1 , s  ,memo)

if __name__ == "__main__":
    s = "T|T&F^T"
    print(coutWaysM(s))
    print(countWays(s))