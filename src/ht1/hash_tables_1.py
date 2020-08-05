words = ['apple', 'book', 'cat', 'dog', 'egypt', 'france']

# what if we had a magic function
# that takes a word --> returns the index for where that word is located in some array
# this function is O(1)

### HASH FUNCTIONS ###
# any string input --> a specific number (within some range)
# IMPT: deterministic (same input will always return the same output)


def my_hash(string, limit):
    # take every character in the string and convert to number
    # convert each character into UTF-8 numbers
    string_utf = string.encode()
    total = 0
    for char in string_utf:
        total += char
        # limit total to 32 bits
        total &= 0xffffffff
    return total % limit


# create an array that is 8 long for our hash table
hash_table = [None] * 8

# add items to hash table using my_hash function
index = my_hash('Hello', len(hash_table))
hash_table[index] = 'Value for Hello'

index = my_hash('world', len(hash_table))
hash_table[index] = 'Value for World'

index = my_hash('card', len(hash_table))
hash_table[index] = 'Value for card'

index = my_hash('apple', len(hash_table))
hash_table[index] = 'Value for apple'

print(hash_table)


# retrieve some items from hash_table
# retrieve the value for 'Hello
index = my_hash('Hello', len(hash_table))
print(hash_table[index])

index = my_hash('card', len(hash_table))
print(hash_table[index])
