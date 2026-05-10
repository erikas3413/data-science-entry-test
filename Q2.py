# Q2

#Task 1

def find_and_replace(lst, find_val, replace_val):
    # Check that lst is a list
    if not isinstance(lst, list): 
        return -1
    
    # Loop through each position in the list
    for i in range(len(lst)):
        # If the item matches find_val, replace it
        if lst[i] == find_val:
            lst[i] = replace_val
    
    # Return the modified list
    return lst

# Task 2

result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)
# Output: [1, 5, 3, 4, 5, 5]

result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)
# Output: ['orange', 'banana', 'orange']