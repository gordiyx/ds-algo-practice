"""
An AVL tree was used to store GDP data for individual quarters.
The following function was implemented: 
    find_gdp(s, year, quarter) – returns the GDP value for the given year and quarter, or a message indicating that the data is not available.
"""
# Inserts a node with a given key and value into the AVL tree
def insert(root, key, val):
    if not root:
        return {"key": key, "val": val, "left": None, "right": None, "height": 1}

    if key < root["key"]:
        root["left"] = insert(root["left"], key, val)
    else:
        root["right"] = insert(root["right"], key, val)

    # Update height
    root["height"] = 1 + max(get_height(root["left"]), get_height(root["right"]))

    # Balance the tree if needed
    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root["left"]["key"]:
        return rotate_right(root)

    # Right Right Case
    if balance < -1 and key > root["right"]["key"]:
        return rotate_left(root)

    # Left Right Case
    if balance > 1 and key > root["left"]["key"]:
        root["left"] = rotate_left(root["left"])
        return rotate_right(root)

    # Right Left Case
    if balance < -1 and key < root["right"]["key"]:
        root["right"] = rotate_right(root["right"])
        return rotate_left(root)

    return root


# Returns the height of a node
def get_height(root):
    return root["height"] if root else 0


# Returns the balance factor of a node
def get_balance(root):
    return get_height(root["left"]) - get_height(root["right"]) if root else 0


# Performs a right rotation
def rotate_right(root):
    new_root = root["left"]
    root["left"] = new_root["right"]
    new_root["right"] = root

    # Update heights
    root["height"] = 1 + max(get_height(root["left"]), get_height(root["right"]))
    new_root["height"] = 1 + max(get_height(new_root["left"]), get_height(new_root["right"]))

    return new_root


# Performs a left rotation
def rotate_left(root):
    new_root = root["right"]
    root["right"] = new_root["left"]
    new_root["left"] = root

    # Update heights
    root["height"] = 1 + max(get_height(root["left"]), get_height(root["right"]))
    new_root["height"] = 1 + max(get_height(new_root["left"]), get_height(new_root["right"]))

    return new_root


# Searches for a node by key
def search(root, key):
    if not root:
        return None
    if root["key"] == key:
        return root
    return search(root["left"], key) if key < root["key"] else search(root["right"], key)


# Returns GDP data for a given year and quarter
def find_gdp(root, year, quarter):
    node = search(root, (year, quarter))
    if node:
        return f"GDP in Q{quarter} {year}: {node['val']}"
    return "Data not available."


# Sample GDP data
data = [
    {"rok": 2022, "ctvrtleti": 1, "hdp": 1.1},
    {"rok": 2021, "ctvrtleti": 2, "hdp": -2.1},
    {"rok": 2022, "ctvrtleti": 4, "hdp": 0.1},
    {"rok": 2021, "ctvrtleti": 3, "hdp": 2.3},
    {"rok": 2021, "ctvrtleti": 4, "hdp": -0.5},
    {"rok": 2022, "ctvrtleti": 2, "hdp": -1.3},
    {"rok": 2022, "ctvrtleti": 3, "hdp": 3.2},
    {"rok": 2021, "ctvrtleti": 1, "hdp": 4.1},
]

# Build the AVL tree
root = None
for entry in data:
    key = (entry["rok"], entry["ctvrtleti"])
    value = entry["hdp"]
    root = insert(root, key, value)

# Example queries
print(find_gdp(root, 2021, 1))  # Should return actual GDP
print(find_gdp(root, 2022, 3))  # Should return actual GDP
print(find_gdp(root, 2023, 1))  # Should return "Data not available."
