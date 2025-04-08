"""
A binary search tree (BST) was used to store WTA ranking points.
The following functions were implemented:
    insert_into_ranking(s, name, points) – inserts a player with the given name and points into the ranking list (BST),
    find_rank(s, k) – prints the player who is ranked k-th in the list s.
"""


# Inserts a player into the WTA ranking BST based on points
def insert_into_ranking(tree, name, points):
    if tree is None:
        return {"name": name, "points": points, "left": None, "right": None, "count": 1}

    if points < tree["points"]:
        tree["left"] = insert_into_ranking(tree["left"], name, points)
    else:
        tree["right"] = insert_into_ranking(tree["right"], name, points)

    # Update the size of the subtree rooted at this node
    tree["count"] = 1
    if tree["left"] is not None:
        tree["count"] += tree["left"]["count"]
    if tree["right"] is not None:
        tree["count"] += tree["right"]["count"]

    return tree


# Finds the player who is ranked k-th (1-based) in the BST
def find_rank(tree, k):
    if tree is None:
        return None

    left_count = tree["left"]["count"] if tree["left"] is not None else 0

    if k == left_count + 1:
        return tree["name"]
    elif k <= left_count:
        return find_rank(tree["left"], k)
    else:
        return find_rank(tree["right"], k - left_count - 1)


# Build the BST with WTA player data
ranking = {"root": None}

ranking["root"] = insert_into_ranking(ranking["root"], "Garcia Caroline", 5000)
ranking["root"] = insert_into_ranking(ranking["root"], "Swiatek Iga", 2597)
ranking["root"] = insert_into_ranking(ranking["root"], "Pegula Jessica", 4340)
ranking["root"] = insert_into_ranking(ranking["root"], "Sabalenka Aryna", 4340)
ranking["root"] = insert_into_ranking(ranking["root"], "Gauff Cori", 3871)
ranking["root"] = insert_into_ranking(ranking["root"], "Kudermetova Veronika", 2715)
ranking["root"] = insert_into_ranking(ranking["root"], "Keys Madison", 2597)
ranking["root"] = insert_into_ranking(ranking["root"], "Sakkari Maria", 3921)
ranking["root"] = insert_into_ranking(ranking["root"], "Jabeur Ons", 5180)
ranking["root"] = insert_into_ranking(ranking["root"], "Kasatkina Darya", 4415)

# Example queries
print("The #1 ranked WTA player is:", find_rank(ranking["root"], 1))
print("The #8 ranked WTA player is:", find_rank(ranking["root"], 8))
