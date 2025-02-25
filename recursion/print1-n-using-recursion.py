# def PrintNUsingRecursion( n : int):
#     if n > 0 :
#         PrintNUsingRecursion(n -1)
#         print(n , end=' ')

# PrintNUsingRecursion(10)

# def PrinitNto1UsingRecursion(n : int):
#     if n ==0 :
#         return
#     print(n , end=" ")
#     PrinitNto1UsingRecursion(n -1)

# PrinitNto1UsingRecursion(10)

# factorial of n!  1 * 2 * 3


# def Factorial(n : int , result):
#     if n == 1 :
#         return result # retun kyu kiya  -> isly taki last wala result mil sake
#     result=result*n
#     return  Factorial(n-1 , result)

    
# def Factorial(n: int):
#     if n == 1:
#         return 1
#     return n * Factorial(n - 1)

# a = Factorial(5)
# print(a)

# a = Factorial(5 , 1)
# print(a)

# Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    return n + fibonacci(n-1)

a = fibonacci(5)
print(a)


# Find the sum of elements in  an array
# a = [1 , 2 , 3 , 4]

# def sumOfArray(a , ind):
#     if ind == len(a):
#         return a[ind]
#     return a[ind] + sumOfArray(a[ind + 1:])

# b = sumOfArray(a )