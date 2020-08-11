records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Pranjal", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing"),
    ("Charles", "Marketing"),
    ("Brian", "Marketing"),
    ("Jordan", "Marketing"),
]

# proposed dictionary
# key: departments
# value: list of names


def build_index(recs):
    index = {}

    for record in recs:
        # unpack and separate
        name, dept = record
        # check if department is already in index
        if dept in index:
            # if key already exists, add name to list
            index[dept].append(name)

        else:
            # else, create new key with list with the name in it
            index[dept] = [name]
    return index


department_index = build_index(records)

# print all the departments
print(department_index.keys())

# print everyone in engineering
print(department_index["Engineering"])

print(department_index)
