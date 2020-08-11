import math

# inverse square root is 1 / square root of a number
# relatively time consuming


def get_inverse_square(num):
    return 1/math.sqrt(num)

# using a lookup table could help a lot if we know we're going to do this over and over for numbers between 1 and 1000


def build_lookup_table():
    lookup_table = {}

    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table


sqrt_lookup_table = build_lookup_table()

print(sqrt_lookup_table[3])
print(sqrt_lookup_table[999])
