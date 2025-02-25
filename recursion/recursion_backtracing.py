
# def generate_subsets(nums):
#     result = []  # To store all subsets

#     def backtrack(index, current):
#         # Base case: if we've considered all elements
#         if index == len(nums):
#             result.append(current[:])  # Add a copy of the current subset
#             return

#         # Choice 1: Include nums[index]
#         current.append(nums[index])
#         backtrack(index + 1, current)

#         # Backtrack: Undo the previous choice
#         current.pop()

#         # Choice 2: Exclude nums[index]
#         backtrack(index + 1, current)

#     backtrack(0, [])
#     return result

# # Test
# print(generate_subsets(['a','b','c']))


# Generate all binary strings of size n.

# Input: 2
# Output:
# 0 0
# 0 1
# 1 0
# 1 1

# TODO : do it again
# def generate_binary_strings(n, result=""):
#     if n == 0:
#         print(result)
#         return
#     # Add '0' and recurse
#     generate_binary_strings(n - 1, result + "0")
#     # Add '1' and recurse
#     generate_binary_strings(n - 1, result + "1")
# # Input
# n = 2
# generate_binary_strings(n)


# TODO : do it again
# def generate_subsets(nums, index=0, current=[]):
#     if index == len(nums):
#         print(current)
#         return
#     # Exclude the current element
#     generate_subsets(nums, index + 1, current)
#     # Include the current element
#     generate_subsets(nums, index + 1, current + [nums[index]])

# # Input
# nums = [1, 2, 3]
# generate_subsets(nums)

# []
# [3]
# [2]
# [2, 3]
# [1]
# [1, 3]
# [1, 2]
# [1, 2, 3]

# Print all permutations of a string.

def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)

# Example usage
string = "ABC"
permute(string)








