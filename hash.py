"""
Historical data from the file ukol-1.txt was stored in a hash table, where the key is the year and the value is the event description.
Double hashing was used as the collision resolution method for inserting values into the hash table.
The search function returns the description of the event if the year is found, or the message "Nothing happened this year." if the key does not exist.
"""


# Primary hash function using built-in hash and modulo
def primary_hash(key, table_size):
    return hash(str(key)) % table_size

# Secondary hash function for double hashing (step size)
def secondary_hash(key, table_size):
    return 1 + (hash(str(key)) % (table_size - 1))

# Inserts a (key, value) pair into the hash table using double hashing
def insert_event(table, key, value):
    index = primary_hash(key, len(table))
    step = secondary_hash(key, len(table))

    # Probe until an empty slot or matching key is found
    while table[index] is not None:
        if table[index][0] == key:
            break  # Update existing
        index = (index + step) % len(table)

    table[index] = (key, value)

# Searches for a year in the hash table and returns the event description
def find_year(table, key):
    index = primary_hash(key, len(table))
    step = secondary_hash(key, len(table))

    while table[index] is not None:
        if table[index][0] == key:
            return table[index][1]
        index = (index + step) % len(table)

    return "Nothing happened this year."


# Initialize hash table
table = [None] * 1000

# Read historical data from file and populate the table
with open("hash.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(';')
        year = int(parts[0])
        description = " ".join(parts[1:])
        insert_event(table, year, description)

# Sample queries
print("Year 650: " + find_year(table, 650))
print("Year 100: " + find_year(table, 100))
