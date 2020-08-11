# substitution ciphers
# or, how to transform data from one thing to another
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

# decode_table = {}

# for key, value in encode_table.items():
#     decode_table[value] = key

decode_table = {value: key for key, value in encode_table.items()}


def encode(plain_text):
    cipher = ""

    for char in plain_text:
        if char.isspace():
            cipher += ' '
        else:
            cipher += encode_table[char.upper()]
    return cipher


def decode(cipher_text):
    plain_text = ""

    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else:
            plain_text += decode_table[char.upper()]
    return plain_text


cipher = encode("Super secret message just for you")
print(cipher)

reversed_plain_text = decode(cipher)
print(reversed_plain_text)
