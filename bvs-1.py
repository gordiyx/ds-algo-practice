
"""
A binary search tree (BST) was used to store a list of people. The key for each node is the person’s name.
The following functions were implemented:
    insert_into_list(s, name) – inserts a person with the given name into the list (BST),
    print_list(s) – prints the list of names in alphabetical order,
    remove_from_list(s, name) – removes the person with the specified name from the list.
"""


# Creates and returns a new BST node with the given key (name)
def create_node(key):
    return {'key': key, 'left': None, 'right': None}


# Inserts a key into the BST and returns the updated root
def insert_node(node, key):
    if node is None:
        return create_node(key)
    if key < node['key']:
        node['left'] = insert_node(node['left'], key)
    elif key > node['key']:
        node['right'] = insert_node(node['right'], key)
    return node


# Performs in-order traversal to print names in alphabetical order
def print_tree(node):
    if node:
        print_tree(node['left'])
        print(node['key'], end=' ')
        print_tree(node['right'])


# Deletes a node with the specified key from the BST
def delete_node(node, key):
    if node is None:
        return node

    if key < node['key']:
        node['left'] = delete_node(node['left'], key)
    elif key > node['key']:
        node['right'] = delete_node(node['right'], key)
    else:
        # Node with only one child or no child
        if node['left'] is None:
            return node['right']
        elif node['right'] is None:
            return node['left']

        # Node with two children: get inorder successor
        temp = min_value_node(node['right'])
        node['key'] = temp['key']
        node['right'] = delete_node(node['right'], temp['key'])

    return node


# Finds the node with the minimum key in a subtree
def min_value_node(node):
    current = node
    while current['left'] is not None:
        current = current['left']
    return current


# Initial list of people
seznam = ["Pavel", "Jitka", "Alice", "Karel", "David"]

# Build the BST from the list
osoby = None
for name in seznam:
    osoby = insert_node(osoby, name)

# Print the full list in alphabetical order
print("Seznam osob:", end=' ')
print_tree(osoby)
print()

# Remove a person from the list
osoby = delete_node(osoby, "Alice")

# Print the updated list
print("Seznam osob:", end=' ')
print_tree(osoby)
