# Dynamic Programming

## V1

1. Recursion - 1. Choice (pick , no pick) 2. Optimal (max , min , smallest , largest ) eg. max profit
2. Dp - 1. Memorization - recursion + Storage 2. Top Down

## V2

3. Types of knapsack
   a. fractional - (Greedy , not dp) can put fractional units
   b. 0/1 knapsack - either the entire unit would be added or it wont be added at all
   c. unbounded - u can add 1 type of unit as many times as u like unlike in 0/1 knapsack whereu u can 1 variety once once.

Analyse the problem is Dp:

1. input - wt [] , value [] , W(capacity) , o/p= amx profit
2. write recurive solution -> memorisation or top down(optional)

Analyse - choice (inclde item1 or not in knapsack)

```
        W1
        / \
    w1<=w  w1>w
    / \      |
x(NP) x  (Not possible)
```

w1<=w = if okay then add the value , if not in those cases where some values were already added in w , and now the left capacity w < w1

format:

```
int knapsack{
    base case
    choice diagram code
}
```

base case:
`if (n==0||w==0) 
     return 0`
-> if the there is no values or knapsack has no capacity the ,max profit is 0

choice diagram -> recursive
choose one value(n-1) remove from input array then keep moving and adding in knapsack and removing from input array

_Base case_

- if the array is empty or W is empty
  -> then no profit
  _if wt<=w then value is added -_
- either add the one which returns max profit ->

1. add price/profit by val[n-1]+knsapsack(wt,val,w-wt[n-1]
2. dont add knapsack(wt,val,w,n-1)

- if wt>w then just return the original profit , just iterate to next array element

```
def knapsack(wt,val,w,n):
    if (n==0 || w==0):
        return 0
    if (wt[n-1]<=w):
        return max(val[n-1]+knsapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
    elif(wt[n-1]>w):
        return knapsack(wt,val,w,n-1)
```

### Top Down -

top down is better than recusive memorisation because for large input it could lead to stack overflow
(mostly memorisation works)

table creation

1. take sizes - n+1 rows and W+1 columns
   wt[]=[1,3,4,5]
   val[]=[1,4,5,7]
   W=7
   t[n+1][W+1] = t[5][8]
2. initialization in first row and first column since we have n+1 row and W+1 columns

W →

| n   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     |     |     |     |     |     |
| 1   |     |     |     |     |     |     |     |     |
| 2   |     |     |     |     |     |     |     |     |
| 3   |     |     |     |     |     |     |     |     |
| 4   |     |     |     |     |     |     |     |     |

| _Top-Down Approach_                             | _Recursive Approach_                                    |
| ----------------------------------------------- | ------------------------------------------------------- |
| _BASE CASE_                                     | _BASE CASE_                                             |
| for i in range(n):                              | if (n == 0 or W == 0):                                  |
| `    for j in range(W):`                        | `    return 0`                                          |
| `        if (i == 0 or j == 0):`                |                                                         |
| `            grid[i][j] = 0`                    |                                                         |
|                                                 |                                                         |
| _CHOICE CONDITION_                              | _CHOICE CONDITION_                                      |
| for i in range(n):                              | if (wt[n-1] <= W):                                      |
| `    for j in range(W):`                        | `    t[n][W] = max(val[n-1] +`                          |
| `        if (wt[i-1] <= j):`                    | `                 knapsack(wt, val, W - wt[n-1], n-1),` |
| `            t[i][j] = max(val[i-1] +`          | `                 knapsack(wt, val, W, n-1))`           |
| `                           t[i-1][j-wt[i-1]],` |                                                         |
| `                           t[i-1][j])`         |                                                         |
| `        else:`                                 | elif (wt[n-1] > W):                                     |
| `            t[i][j] = t[i-1][j]`               | `    t[n][W] = knapsack(wt, val, W, n-1)`               |
