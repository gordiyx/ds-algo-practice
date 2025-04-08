"""
A tree structure (as shown in the diagram) has been implemented using a structure where children are stored in a list using the following definition:
A depth-first traversal function has been implemented for this tree structure.
"""

# Tree node structure:
# Each node contains:
#   - "id": unique identifier
#   - "child": reference to its first child
#   - "sibling": reference to the next sibling

# Depth-First Search (DFS) traversal function
# Visits a node, then recursively visits its children and siblings
def depth_first_search(node):
    if node is not None:
        print(node["id"], end=" ")           # Visit current node
        depth_first_search(node["child"])    # Traverse first child
        depth_first_search(node["sibling"])  # Traverse next sibling


# Tree structure defined using nested dictionaries
root = {
    "id": 1,
    "child": {
        "id": 2,
        "child": {
            "id": 5,
            "child": None,
            "sibling": {
                "id": 6,
                "child": {
                    "id": 10,
                    "child": None,
                    "sibling": {
                        "id": 11,
                        "child": None,
                        "sibling": {
                            "id": 12,
                            "child": None,
                            "sibling": None
                        }
                    }
                },
                "sibling": {
                    "id": 7,
                    "child": None,
                    "sibling": None
                }
            }
        },
        "sibling": {
            "id": 3,
            "child": None,
            "sibling": {
                "id": 4,
                "child": {
                    "id": 8,
                    "child": None,
                    "sibling": {
                        "id": 9,
                        "child": None,
                        "sibling": None
                    }
                },
                "sibling": None
            }
        }
    },
    "sibling": None
}

# Execute depth-first traversal
depth_first_search(root)
