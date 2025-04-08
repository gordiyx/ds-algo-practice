"""
Historical data from the file ukol-1.txt has been stored in an array, where the key is the year and the value is a description of the event.
For searching within the array, the binary search algorithm was used.
The search function returns the event description if the year is found in the array, or the message "Nothing happened this year." if not.
"""


# Creates a fixed-size array structure to store historical records
def create_array(n):
    records = [{"key": None, "data": None} for _ in range(n)]
    return {"keys": records, "top": 0}  # 'top' tracks the current number of entries

# Inserts a new record into the array if there's space
def insert(arr, record):
    if arr["top"] < len(arr["keys"]):
        arr["keys"][arr["top"]] = record
        arr["top"] += 1

# Performs binary search on the sorted array to find a record by year
def binary_search(arr, year):
    left = 0
    right = arr["top"] - 1

    while left <= right:
        mid = (left + right) // 2
        mid_key = arr["keys"][mid]["key"]

        if mid_key == year:
            return arr["keys"][mid]["data"]
        elif mid_key < year:
            left = mid + 1
        else:
            right = mid - 1

    return "Nothing happened this year."


# Load historical data from a text file into the array
record_count = 50
array_set = create_array(record_count)

with open("linearni_datove_struktury_1.txt", "rt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        year = int(parts[0])
        description = parts[1]
        insert(array_set, {"key": year, "data": description})

# IMPORTANT: Binary search requires the array to be sorted by key (year)
array_set["keys"] = sorted(array_set["keys"][:array_set["top"]], key=lambda x: x["key"])
array_set["top"] = len(array_set["keys"])  # Update 'top' after sorting

# Sample searches
print("Year 371: " + binary_search(array_set, 371))
print("Year 100: " + binary_search(array_set, 100))
