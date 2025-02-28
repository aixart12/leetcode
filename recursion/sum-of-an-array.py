# def sumOfArray(a , ind):
#     if len(a) == 0:
#         return 0
#     else : 
#         if ind == len(a) - 1:
#             return a[ind]
#         return a[ind] + sumOfArray(a , ind = ind + 1)

# print(sumOfArray([1 ] , 0))


# def findMaxInArray(arr , ind , res):
#     if ind == len(arr) -1:
#         if arr[ind] > res : 
#             return arr[ind]
#         else:
#             return res
#     if(arr[ind] > res):
#         res = arr[ind]
#     return findMaxInArray(arr , ind =ind + 1  , res=res )

# print(findMaxInArray([1 , 4, 2 ] , 0 , -1))


def checkIFArrayisSorte(arr , ind):
    if ind  == len(arr) - 2:
        if arr[ind] < arr[ind + 1]:
            return True 
        else : 
            return False
    
    if arr[ind] > arr[ind + 1]:
        return False
    return checkIFArrayisSorte(arr , ind = ind + 1)

i = [1, 2, 3, 5, 5, 7, 7, 7, 8, 12, 13, 15, 15, 15, 19]


print(checkIFArrayisSorte(i, 0))
# Count occurrences of an element in an array.
# def countElimentOccurrenece(arr , target , count , ind):
#     if ind == len(arr) -1 :
#         if arr[ind] == target:
#             count+=1
#             return count
#         else:
#             return count
        
#     if(arr[ind] == target):
#         count+=1
#     return countElimentOccurrenece(arr , target , count , ind = ind + 1)

# print(countElimentOccurrenece([ 1 ,1 , 1] , 1 , 0 , 0))


