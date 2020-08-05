words = ['apple', 'book', 'cat', 'dog', 'egypt', 'france']

# what if we had a magic function
# that takes a word --> returns the index for where that word is located in some array
# this function is O(1)

### HASH FUNCTIONS ###
# any string input --> a specific number (within some range)
# IMPT: deterministic (same input will always return the same output)


def my_hash(string):
    # take every character in the string and convert to number
    # convert each character into UTF-8 numbers
    string_utf = string.encode()
    total = 0
    for char in string_utf:
        total += char
    return total


print(my_hash("hello"))
