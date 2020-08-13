"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

e.g.
Input: J = "aA", S = "aAAbbbb"
Output: 3

Input: J = "z", S = "ZZ"
Output: 0
"""


# naive solution O(n^2)
def naiveNumJewelsInStones(J, S):
    count = 0
    for char_j in J:
        for char_s in S:
            if char_j == char_s:
                count += 1
    return count


# improved solution O(3n) -> O(n)
def numJewelsInStones(J, S):
    jewels_dict = {}
    count = 0
    for char_j in J:
        jewels_dict[char_j] = 0

    for char_s in S:
        if char_s in jewels_dict:
            count += 1

    return count


J = "aA"
S = "aAAbbbb"
print(naiveNumJewelsInStones(J, S))
print(numJewelsInStones(J, S))
