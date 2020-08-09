class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


hash_table = [None] * 8  # 8 slots, all initialized to None


def my_hash(string):
    # take every character in the string and convert to number
    # convert each character into UTF-8 numbers
    string_utf = string.encode()
    total = 0
    for char in string_utf:
        total += char
        # limit total to 32 bits
        total &= 0xffffffff
    return total


def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)


def put(key, value):
    # hash the key and get an index
    i = hash_index(key)
    # find the start of the linked list using the index
    # search through the linked list
    # if the key already exists
    # overwrite the value
    # else
    # add new HashTableEntry into the head (or tail) of linked list


def get(key):
    # hash the key and get an index
    i = hash_index(key)
    # get the linked list at the computed index
    # search through the linked list for the key
    # if key exists
    # return the value
    # else
    # return None


def delete(key):
    # hash the key and get an index
    i = hash_index(key)
    # search through the linked list for the matching key
    # if key exists
    # save value
    # delete
    # return value


def resize():
    # make a new array thats DOUBLE the current size
    # go through each linked list in the array
    # re-hash each item
    # insert the items into the new array
    pass


def downsize():
    # make a new array thats HALF the current size
    # go through each linked list in the array
    # re-hash each item
    # insert the items into the new array
    pass


put("Hello", "Hello Value")
put("foo", "foo Value")
put("World", "World Value")
print(get("Hello"))

print(hash_table)
