"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

e.g.
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


seen_values = set()


def isHappy(n):
    # base cases
    if n == 1:
        return True
    elif n in seen_values:
        return False

    # recursive case
    # store n into a cache (it is known)
    seen_values.add(n)
    # transform n into new value
    # break into digits, square each digit, sum squares
    new_num = sum([int(digit)**2 for digit in str(n)])

    # recurse with new value
    return isHappy(new_num)


print(isHappy(19))  # true
print(isHappy(4))  # false
