"""
A B-Tree was used to store maximum temperature data for each day of the year.
The following function was implemented:
    find_temperature(s, day) – returns the maximum temperature for the specified day, if available.
"""

# Degree of the B-Tree (minimum degree T)
T = 2

# Creates and returns a new B-Tree node
def create_node(leaf=False):
    return {
        'leaf': leaf,       # True if node is a leaf
        'keys': [],         # List of keys (e.g. days)
        'values': [],       # Associated values (e.g. temperatures)
        'children': []      # List of child nodes
    }

# Searches for a key in the B-Tree and returns the associated value, or None if not found
def search(node, key):
    i = 0
    while i < len(node['keys']) and key > node['keys'][i]:
        i += 1
    if i < len(node['keys']) and key == node['keys'][i]:
        return node['values'][i]
    if node['leaf']:
        return None
    return search(node['children'][i], key)

# Inserts a key-value pair into the B-Tree (simplified; doesn't fully implement B-Tree splits)
def insert(node, key, value):
    i = 0
    while i < len(node['keys']) and key > node['keys'][i]:
        i += 1
    if node['leaf']:
        node['keys'].insert(i, key)
        node['values'].insert(i, value)
    else:
        # Simplified handling; does not implement full B-Tree balancing
        if len(node['children'][i]) == 2*T - 1:
            # Placeholder split logic (not fully implemented)
            split_node = create_node(leaf=False)
            split_node['children'].append(node['children'][i])
            split_node['keys'].append(node['keys'][i])
            split_node['values'].append(node['values'][i])
            node['children'][i] = split_node
            node['keys'].insert(i, key)
            node['values'].insert(i, value)
            node['children'].insert(i+1, create_node(leaf=True))
            split_node_index = i + 1 if key > node['keys'][i] else i
        else:
            split_node_index = i
        insert(node['children'][split_node_index], key, value)

# Returns the max temperature for a given day, or a not-found message
def find_temperature(root, day):
    value = search(root, day)
    if value is not None:
        return f"Maximum temperature on {day} was {value}°C."
    return f"Maximum temperature on {day} was not found."


# Initialize root node
root = create_node(leaf=True)

# Sample temperature data by day
data = [
    {"den": "1.1.", "teplota": 1.1},
    {"den": "12.12.", "teplota": 2.3},
    {"den": "8.7.", "teplota": 20.1},
    {"den": "14.3.", "teplota": 4.3},
    {"den": "17.11.", "teplota": 8.1},
    {"den": "12.4.", "teplota": 6.2},
    {"den": "17.11.", "teplota": 3.8},   # Duplicate key – this will overwrite the previous value
    {"den": "19.12.", "teplota": 1.8},
    {"den": "1.9.", "teplota": 12.3},
    {"den": "13.8.", "teplota": 19.6},
    {"den": "14.2.", "teplota": 2.2},
    {"den": "16.5.", "teplota": 10.7},
    {"den": "14.5.", "teplota": 10.5},
    {"den": "5.10.", "teplota": 6.2},
    {"den": "18.12.", "teplota": 0.4},
    {"den": "12.6.", "teplota": 13.1},
]

# Insert data into the B-Tree
for item in data:
    insert(root, item["den"], item["teplota"])

# Example queries
print(find_temperature(root, "5.10."))   # Should return a value
print(find_temperature(root, "31.12."))  # Should return "not found"
