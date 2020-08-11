#  given a string, can we figure out how many times each letter appears in it?

def letter_count(string):
    # dict where keys are letters and values will be an incrementing counter
    d = {}
    for char in string:
        if char.isspace():
            continue
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


# print(letter_count("aaabbc"))
# print(letter_count("Hello!"))
# print(letter_count("The quick brown fox jumps over the lazy dog"))

# return letters that appear twice in a string
def double_letter(string):
    # store letters as keys, count as value
    d = set()
    for char in string:
        if char.isspace():
            continue
        if char not in d:
            d.add(char)
        else:
            return char


print(double_letter("abcdeef"))
