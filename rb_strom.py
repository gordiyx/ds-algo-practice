"""
A Red-Black Tree was used to store the number of points earned by students.
The following functions were implemented:
    add_points(s, name, points) – inserts a student with the given name and points into the tree. If the student already exists, the points are added to their total.
    total_points(s, name) – returns the total number of points for the specified student, or a message indicating that the student is not in the list.
"""


# Red-Black Tree color definitions
RED = True
BLACK = False

# Creates a new Red-Black Tree node
def create_node(key, value, color=RED, left=None, right=None):
    return {"key": key, "value": value, "color": color, "left": left, "right": right}

# Checks if a node is red (used for balancing)
def is_red(node):
    return node is not None and node["color"] == RED

# Left rotation to balance right-leaning red links
def rotate_left(node):
    new_node = node["right"]
    node["right"] = new_node["left"]
    new_node["left"] = node
    new_node["color"] = node["color"]
    node["color"] = RED
    return new_node

# Right rotation to balance consecutive left-leaning red links
def rotate_right(node):
    new_node = node["left"]
    node["left"] = new_node["right"]
    new_node["right"] = node
    new_node["color"] = node["color"]
    node["color"] = RED
    return new_node

# Color flip to split 4-nodes
def flip_colors(node):
    node["color"] = RED
    node["left"]["color"] = BLACK
    node["right"]["color"] = BLACK

# Inserts or updates a node in the Red-Black Tree
def pridej_body(node, name, points):
    if node is None:
        return create_node(name, points, BLACK)  # First node is black (root)

    if name < node["key"]:
        node["left"] = pridej_body(node["left"], name, points)
    elif name > node["key"]:
        node["right"] = pridej_body(node["right"], name, points)
    else:
        node["value"] += points  # Update existing student's score
        return node

    # Rebalancing the tree
    if is_red(node["right"]) and not is_red(node["left"]):
        node = rotate_left(node)
    if is_red(node["left"]) and is_red(node["left"]["left"]):
        node = rotate_right(node)
    if is_red(node["left"]) and is_red(node["right"]):
        flip_colors(node)

    return node

# Searches for a student by name and returns their score
def get(node, key):
    while node is not None:
        if key < node["key"]:
            node = node["left"]
        elif key > node["key"]:
            node = node["right"]
        else:
            return node["value"]
    return None

# Prints the total score for the given student name
def body_celkem(node, name):
    points = get(node, name)
    if points is not None:
        print(f"Student {name} has {points} points.")
    else:
        print(f"Student {name} is not in the list.")


# Sample usage
t = None
t = pridej_body(t, "Pavel", 2)
t = pridej_body(t, "Jirka", 1)
t = pridej_body(t, "Alena", 3)
t = pridej_body(t, "Pavel", 4)
t = pridej_body(t, "Pavel", 6)
t = pridej_body(t, "Jirka", 2)

body_celkem(t, "Pavel")   # Should output total points for Pavel
body_celkem(t, "Karel")   # Should say student not found
