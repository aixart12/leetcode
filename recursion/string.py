# def reverseAstring(s : str):
#     if len(s) == 0 : 
#         return ""
#     reverseAstring(s[1:])
#     return  reverseAstring(s[1:]) + s[0]
# print(reverseAstring('hiwe'))


# # Check if a string is a palindrome.

# def checkIfStringIsPalindrom(s : str):
#     #  chekc first and last index 
#     #  if equal slice both at end and at last
#     #  if not equl return false
#     n = len(s)
#     if not s: 
#         return True
#     if s[0] == s[n-1]:
#         s = s[1:n-1]
#         return checkIfStringIsPalindrom(s)
#     else:
#         return False
# print(checkIfStringIsPalindrom('asaa'))

# def checkStrIsPalindromTwo(s : str , i : int):
#     n = len(s)
#     if not s:
#         return True
#     if i > n/2:
#         return True
#     if s[i] != s[n-1-i]:
#         return False
#     return checkStrIsPalindromTwo(s , i= i +1)

# print(checkStrIsPalindromTwo('a' , 0))


# Count vowels in a string
# def countVovels(s : str ,r ,  i ):
#     if i == len(s):
#         return r
#     if s[i] in ['a','e','i' , 'o' , 'u']:
#         r = r+1
#     return countVovels(s,r , i=i +1 )

# print(countVovels('g' , 0 , 0))


def printSubstrings(s):
    def helper(i, current):
        if i == len(s):  # Base case: Stop when index reaches the end
            if current:  # Avoid printing empty string
                print(current)
            return
        
        # Pick the current character
        helper(i + 1, current + s[i])
        
        # No Pick (Start a new substring)
        if current:  # Ensures we start fresh only when needed
            return
        
        # Start a new substring from next index
        helper(i + 1, "")

    helper(0, "")  # Start from index 0 with an empty string

# Example Usage
s = "abc"
printSubstrings(s)